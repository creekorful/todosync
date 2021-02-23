import os
import unittest

from todosync import database


class MyTestCase(unittest.TestCase):
    def test_load_save(self):
        tasks = [
            {'remote_id': 1414, 'todoist_item_id': 'abaca111'},
            {'remote_id': 4242, 'todoist_item_id': 'abaca222'},
        ]

        database.save_tasks('test.db', tasks)
        self.assertTrue(os.path.exists('test.db'))

        loaded_tasks = database.load_tasks('test.db')
        self.assertEqual(2, len(loaded_tasks))
        self.assertListEqual(loaded_tasks, tasks)

        os.remove('test.db')

        pass


if __name__ == '__main__':
    unittest.main()
