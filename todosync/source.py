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
                'gitlab_issue_id': issue.id,
                'gitlab_project_id': issue.project_id,
                'title': issue.title,
                'description': issue.description,
                'due_date': issue.due_date
            })

    return tasks
