import unittest

from todosync.source import gitlab


class MyTestCase(unittest.TestCase):
    def test_get_gitlab_url(self):
        obj = type('obj', (object,), {
            'references': {
                "short": "#7",
                "relative": "#7",
                "full": "creekorful/test#7"
            },
        })

        self.assertEqual("https://gitlab.com/creekorful/test", gitlab.get_gitlab_url(obj))

    def test_get_gitlab_status(self):
        obj = type('obj', (object,), {
            'assignee': None,
        })
        self.assertEqual("todo", gitlab.get_status(obj))

        obj = type('obj', (object,), {
            'assignee': {},
        })
        self.assertEqual("in_progress", gitlab.get_status(obj))

        pass


if __name__ == '__main__':
    unittest.main()
