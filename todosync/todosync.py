import todoist
import toml
from rich import print

from todosync import database
from todosync.source import gitlab, github


def compute_changes(previous: list[dict], current: list[dict]) -> (list[dict], list[dict], list[dict]):
    """
    Compute the new/closed tasks
    :param previous the previous list of tasks
    :param current the current retrieved list of tasks
    :return the new tasks, the updated ones and the closed ones
    """

    new_tasks = []
    updated_tasks = []
    closed_tasks = []

    # search for new & updated tasks
    for current_task in current:
        found = False
        for previous_task in previous:
            if previous_task['remote_id'] == current_task['remote_id'] and \
                    previous_task['kind'] == current_task['kind']:
                found = True

                if previous_task['status'] != current_task['status']:
                    # todoist_item_id should be returned to allow task update
                    current_task['todoist_item_id'] = previous_task['todoist_item_id']
                    updated_tasks.append(current_task)

                break

        if not found:
            new_tasks.append(current_task)

    # search for closed tasks
    for previous_task in previous:
        found = False
        for current_task in current:
            if current_task['remote_id'] == previous_task['remote_id'] and \
                    previous_task['kind'] == current_task['kind']:
                found = True
                break

        if not found:
            closed_tasks.append(previous_task)

    return new_tasks, updated_tasks, closed_tasks


def get_config(config: dict, url: str) -> (list[int], int, int):
    """
    Get the config for given source url
    :param config the current config
    :param url the source url
    :return labels, todo section id, in_progress section id
    """

    if 'sources' not in config:
        raise Exception("No sources")

    if url not in config['sources']:
        raise Exception("Source not found")

    src = config['sources'][url]

    labels = []
    if 'labels' in src:
        labels = src['labels']

    # merge with default labels
    if 'default_labels' in config['config']:
        labels.extend(config['config']['default_labels'])

    if 'todo' in src:
        todo = src['todo']
    else:
        todo = src['default']

    if 'in_progress' in src:
        in_progress = src['in_progress']
    else:
        in_progress = src['default']

    return labels, todo, in_progress


def synchronize(dry_run: bool):
    """
    Main entrypoint of `todosync`
    This perform the synchronization Gitlab <=> Todoist

    :param dry_run: shall we commit & save the changes?
    """

    config = toml.load('config.toml')

    sources_url = config['sources'].keys()

    # load previous tasks from the database
    previous_tasks = database.load_tasks(config['config']['database_file'])

    # then retrieve the remote issues
    issues = []

    if 'gitlab_token' in config['config']:
        issues.extend(gitlab.retrieve_issues(config['config']['gitlab_token'], sources_url))
    if 'github_token' in config['config']:
        issues.extend(github.retrieve_issues(config['config']['github_token'], sources_url))

    # compute the new, updated & closed tasks
    new_tasks, updated_tasks, closed_tasks = compute_changes(previous_tasks, issues)

    if not new_tasks and not updated_tasks and not closed_tasks:
        print("[bold yellow]Nothing to synchronize![/bold yellow]")
        return

    print("[bold green]{}[/bold green] new tasks".format(len(new_tasks)))
    print("[bold yellow]{}[/bold yellow] updated tasks".format(len(updated_tasks)))
    print("[bold red]{}[/bold red] closed tasks".format(len(closed_tasks)))
    print("")

    # instantiate Todoist client
    todoist_api = todoist.TodoistAPI(config['config']['todoist_token'])
    todoist_api.sync()

    # close the closed tasks
    for task in closed_tasks:
        print("[bold red]Closing[/bold red] task {} - {}".format(task['todoist_item_id'], task['title']))

        todoist_api.items.delete(task['todoist_item_id'])

    # update the updated task
    for task in updated_tasks:
        print("[bold yellow]Updating[/bold yellow] task {} - {}".format(task['todoist_item_id'], task['title']))

        labels, todo, in_progress = get_config(config, task['remote_url'])

        section_id = in_progress if task['status'] == 'in_progress' else todo

        todoist_api.items.move(task['todoist_item_id'], section_id=section_id)

    # then create the new tasks
    for task in new_tasks:
        print("[bold green]Creating[/bold green] task `{}`".format(task['title']))

        labels, todo, in_progress = get_config(config, task['remote_url'])

        section_id = in_progress if task['status'] == 'in_progress' else todo

        due = {}
        if task['due_date'] is not None:
            due = {'date': task['due_date']}

        item = todoist_api.items.add(task['title'], section_id=section_id, labels=labels, due=due)
        task['todoist_item_id'] = item['id']

    if not dry_run:
        todoist_api.commit()

        # update the local database with the tasks refreshed
        database.save_tasks(config['config']['database_file'], new_tasks, updated_tasks, closed_tasks)
    else:
        print("[bold yellow]Not synchronizing (--dry-run)[/bold yellow]")
