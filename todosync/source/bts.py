import html

import requests
from bs4 import BeautifulSoup


def retrieve_issues(source_urls: list[str]) -> list[dict]:
    issues = []

    for source_url in source_urls:
        if source_url.startswith('https://bugs.debian.org/'):
            r = requests.get(source_url)
            issue = parse_bug(r.text)

            if issue['status'] != 'done':
                issues.append(issue)

    return issues


def parse_bug(html_str: str) -> dict:
    parsed_html = BeautifulSoup(html_str, features="html.parser")

    # extract title (belongs to h1 div)
    h1_line = parsed_html.body.find('h1')

    bug_number = str(h1_line.find('a').text).replace("#", "")
    clean_title = str(h1_line).split("<br/>")[1].replace("</h1>", "").replace("\n", "")

    # extract buginfo
    buginfo = str(parsed_html.body.find('div', attrs={'class': 'buginfo'}))

    # parse bug_status (todo improve)
    bug_status = 'todo'
    if '<strong>Done:</strong>' in buginfo:
        bug_status = 'done'
    elif '<p>Owned by: ' in buginfo:
        bug_status = 'in_progress'

    return {
        'remote_id': int(bug_number),
        'remote_url': "https://bugs.debian.org/{}".format(bug_number),
        'title': html.unescape(clean_title),
        'description': '',  # todo
        'due_date': None,
        'status': bug_status,
        'kind': 'bts'
    }
