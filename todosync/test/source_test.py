import unittest

from todosync.source import get_gitlab_url


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


if __name__ == '__main__':
    unittest.main()
