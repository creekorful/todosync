import unittest

from todosync.todosync import compute_changes, get_config


class MyTestCase(unittest.TestCase):
    def test_compute_changes_no_changes(self):
        a, b, c = compute_changes([], [])
        self.assertEqual(0, len(a))
        self.assertEqual(0, len(b))
        self.assertEqual(0, len(c))

    def test_compute_changes(self):
        previous = [
            {'todoist_item_id': '12', 'remote_id': 1, 'status': 'todo', 'kind': 'gitlab'},
            {'todoist_item_id': '42', 'remote_id': 2, 'status': 'todo', 'kind': 'gitlab'}
        ]
        current = [
            {'remote_id': 1, 'status': 'in_progress', 'kind': 'gitlab'},
            {'remote_id': 4, 'status': 'todo', 'kind': 'gitlab'}
        ]

        new, updated, closed = compute_changes(previous, current)
        self.assertEqual(1, len(new))
        self.assertEqual(1, len(updated))
        self.assertEqual(1, len(closed))

        self.assertEqual(4, new[0]['remote_id'])
        self.assertEqual(1, updated[0]['remote_id'])
        self.assertEqual('12', updated[0]['todoist_item_id'])  # should be returned
        self.assertEqual(2, closed[0]['remote_id'])

    def test_get_config_url_no_sources(self):
        with self.assertRaises(Exception):
            config = {}

            get_config(config, 'https://gitlab.com/creekorful/test')

    def test_get_config_url_not_present(self):
        with self.assertRaises(Exception):
            config = {'sources': {}}

            get_config(config, 'https://gitlab.com/creekorful/test')

    def test_get_config_missing_todo(self):
        config = {
            'config': {},
            'sources': {
                "https://gitlab.com/creekorful/test": {
                    'url': 'https://gitlab.com/creekorful/test',
                    'default': 42,
                    'in_progress': 2424,
                }
            }}

        labels, todo, in_progress = get_config(config, 'https://gitlab.com/creekorful/test')

        self.assertEqual([], labels)
        self.assertEqual(42, todo)
        self.assertEqual(2424, in_progress)

    def test_get_config_missing_in_progress(self):
        config = {
            'config': {},
            'sources': {
                "https://gitlab.com/creekorful/test": {
                    'url': 'https://gitlab.com/creekorful/test',
                    'default': 42,
                    'todo': 2424,
                }
            }}

        labels, todo, in_progress = get_config(config, 'https://gitlab.com/creekorful/test')

        self.assertEqual([], labels)
        self.assertEqual(2424, todo)
        self.assertEqual(42, in_progress)

    def test_get_config_no_default_missing_todo(self):
        with self.assertRaises(Exception):
            config = {
                'config': {},
                'sources': {
                    "https://gitlab.com/creekorful/test": {
                        'url': 'https://gitlab.com/creekorful/test',
                        'in_progress': 2424,
                    }
                }}

            get_config(config, 'https://gitlab.com/creekorful/test')

    def test_get_config_no_default_missing_in_progress(self):
        with self.assertRaises(Exception):
            config = {
                'config': {},
                'sources': {
                    "https://gitlab.com/creekorful/test": {
                        'url': 'https://gitlab.com/creekorful/test',
                        'todo': 2424,
                    }
                }}

            get_config(config, 'https://gitlab.com/creekorful/test')

    def test_get_config(self):
        config = {
            'config': {},
            'sources': {
                "https://gitlab.com/creekorful/test": {
                    'url': 'https://gitlab.com/creekorful/test',
                    'default': 42,
                    'todo': 2121,
                    'in_progress': 2424,
                }
            }}

        labels, todo, in_progress = get_config(config, 'https://gitlab.com/creekorful/test')

        self.assertEqual([], labels)
        self.assertEqual(2121, todo)
        self.assertEqual(2424, in_progress)

    def test_get_config_with_default_labels(self):
        config = {
            'config': {
                'default_labels': [12]
            },
            'sources': {
                "https://gitlab.com/creekorful/test": {
                    'url': 'https://gitlab.com/creekorful/test',
                    'labels': [6, 24],
                    'default': 42,
                    'todo': 2121,
                    'in_progress': 2424,
                }
            }}

        labels, todo, in_progress = get_config(config, 'https://gitlab.com/creekorful/test')

        self.assertEqual([6, 24, 12], labels)
        self.assertEqual(2121, todo)
        self.assertEqual(2424, in_progress)


if __name__ == '__main__':
    unittest.main()
