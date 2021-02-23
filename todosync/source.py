import gitlab


def retrieve_gitlab_issues(token: str) -> list[dict]:
    """
    Retrieve the user issues from gitlab.com
    :type token: the Gitlab auth token to identify the user
    :return: list of users opened issues, mapped as tasks
    """

    tasks = []

    with gitlab.Gitlab("https://gitlab.com", private_token=token) as gl:
        issues = gl.issues.list(state='opened')
        for issue in issues:
            tasks.append({
                'remote_id': issue.id,
                'title': issue.title,
                'description': issue.description,
                'due_date': issue.due_date,
                'status': get_gitlab_status(issue),
                'url': get_gitlab_url(issue)
            })

    return tasks


def get_gitlab_url(issue) -> str:
    slug = issue.references['full'].replace(issue.references['short'], '')
    return "https://gitlab.com/{}".format(slug)


def get_gitlab_status(issue) -> str:
    return 'in_progress' if 'Doing' in issue.labels else 'todo'
