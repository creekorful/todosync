from github import Github


def retrieve_issues(token: str, source_urls: list[str]) -> list[dict]:
    """
    Retrieve the user issues from github.com
    :type token: the Github auth token to identify the user
    :type source_urls: the list of sources URLs
    :return: list of users opened issues, mapped as tasks
    """

    g = Github(token)

    tasks = []

    repositories = get_repositories(source_urls)
    if len(repositories) == 0:
        return []

    # create Github search query
    query = "type:issue is:open"
    for repository in repositories:
        query = query + " repo:{}".format(repository)

    for issue in g.search_issues(query):
        tasks.append({
            'remote_id': issue.id,
            'remote_url': issue.repository.html_url,
            'title': issue.title,
            'description': issue.body,
            'due_date': None,
            'status': get_status(issue),
            'kind': 'github'
        })

    return tasks


def get_status(issue) -> str:
    return 'in_progress' if issue.assignee is not None else 'todo'


def get_repositories(source_urls: list[str]) -> list[str]:
    repositories = []

    for source_url in source_urls:
        if 'github.com' in source_url:
            repositories.append(source_url.replace('https://github.com/', ''))

    return repositories
