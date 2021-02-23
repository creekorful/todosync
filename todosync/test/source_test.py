import unittest

from todosync.source import get_gitlab_url, get_gitlab_status


class MyTestCase(unittest.TestCase):
    def test_get_gitlab_url(self):
        obj = type('obj', (object,), {
            'references': {
                "short": "#7",
                "relative": "#7",
                "full": "creekorful/test#7"
            },
        })

        self.assertEqual("https://gitlab.com/creekorful/test", get_gitlab_url(obj))

    def test_get_gitlab_status(self):
        obj = type('obj', (object,), {
            'labels': [],
        })
        self.assertEqual("todo", get_gitlab_status(obj))

        obj = type('obj', (object,), {
            'labels': ['Doing', 'feature'],
        })
        self.assertEqual("in_progress", get_gitlab_status(obj))

        pass


if __name__ == '__main__':
    unittest.main()
