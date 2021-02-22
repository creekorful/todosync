import unittest

from todosync.todosync import compute_changes


class MyTestCase(unittest.TestCase):
    def test_compute_changes_no_changes(self):
        a, b = compute_changes([], [])
        self.assertEqual(0, len(a))
        self.assertEqual(0, len(b))

    def test_compute_changes(self):
        previous = [
            {'gitlab_issue_id': 1}, {'gitlab_issue_id': 2}
        ]
        current = [
            {'gitlab_issue_id': 1}, {'gitlab_issue_id': 4}
        ]

        new, closed = compute_changes(previous, current)
        self.assertEqual(1, len(new))
        self.assertEqual(1, len(closed))

        self.assertEqual(4, new[0]['gitlab_issue_id'])
        self.assertEqual(2, closed[0]['gitlab_issue_id'])


if __name__ == '__main__':
    unittest.main()
