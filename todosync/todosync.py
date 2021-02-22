import todoist
import toml
from rich import print

from todosync import database, source


def compute_changes(previous: list[dict], current: list[dict]) -> (list[dict], list[dict]):
    """
    Compute the new/closed tasks
    :param previous the previous list of tasks
    :param current the current retrieved list of tasks
    :return the new tasks and the closed ones
    """

    new_tasks = []
    closed_tasks = []

    # search for closed tasks
    for previous_task in previous:
        found = False
        for current_task in current:
            if current_task['gitlab_issue_id'] == previous_task['gitlab_issue_id']:
                found = True
                break

        if not found:
            closed_tasks.append(previous_task)

    # search for new tasks
    for current_task in current:
        found = False
        for previous_task in previous:
            if previous_task['gitlab_issue_id'] == current_task['gitlab_issue_id']:
                found = True
                break

        if not found:
            new_tasks.append(current_task)

    return new_tasks, closed_tasks


def synchronize():
    """
    Main entrypoint of `todosync`
    This perform the synchronization Gitlab <=> Todoist
    """

    config = toml.load('config.toml')

    # load existing tasks from the database
    tasks = database.load_tasks(config['database_file'])

    # then retrieve the Gitlab issues
    gitlab_issues = source.retrieve_gitlab_issues(config['gitlab_token'])

    # compute the new & closed tasks
    new_tasks, closed_tasks = compute_changes(tasks, gitlab_issues)

    if not new_tasks and not closed_tasks:
        print("[bold yellow]Nothing to synchronize![/bold yellow]")
        return

    print("[bold green]{}[/bold green] new tasks".format(len(new_tasks)))
    print("[bold red]{}[/bold red] closed tasks".format(len(closed_tasks)))
    print("")

    # instantiate Todoist client
    todoist_api = todoist.TodoistAPI(config['todoist_token'])
    todoist_api.sync()

    # close the closed tasks
    for task in closed_tasks:
        print("[bold red]Closing[/bold red] task #{} - {}", task['todoist_id'], task['title'])

        todoist_api.items.delete(task['todoist_item_id'])

    # then create the new tasks
    for task in new_tasks:
        print("[bold green]Creating[/bold green] task `{}`".format(task['title']))

        item = todoist_api.items.add(task['title'])
        task['todoist_item_id'] = item['id']

    todoist_api.commit()

    # update the local database
    database.save_tasks(config['database_file'], new_tasks)
