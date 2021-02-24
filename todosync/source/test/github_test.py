import unittest

from todosync.source import github


class MyTestCase(unittest.TestCase):
    def test_get_github_status(self):
        obj = type('obj', (object,), {
            'assignee': None,
        })
        self.assertEqual('todo', github.get_status(obj))

        obj = type('obj', (object,), {
            'assignee': {},
        })
        self.assertEqual('in_progress', github.get_status(obj))

    def test_get_repositories(self):
        sources_url = [
            'https://github.com/creekorful/todosync',
            'https://gitlab.com/creekorful/test',
            'https://github.com/creekorful/mvnparser'
        ]
        self.assertEqual(['creekorful/todosync', 'creekorful/mvnparser'], github.get_repositories(sources_url))


if __name__ == '__main__':
    unittest.main()
