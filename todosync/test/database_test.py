import os
import unittest

from todosync import database


class MyTestCase(unittest.TestCase):
    def test_load_save(self):
        # create initial tasks
        new_tasks = [
            {'remote_id': 1414, 'todoist_item_id': 'abaca111', 'title': 'task #1', 'kind': 'gitlab', 'status': 'todo'},
            {'remote_id': 4242, 'todoist_item_id': 'abaca222', 'title': 'task #2', 'kind': 'gitlab', 'status': 'todo'},
            {'remote_id': 2727, 'todoist_item_id': 'abaca222', 'title': 'task #3', 'kind': 'github', 'status': 'todo'},
        ]
        database.save_tasks('test.db', new_tasks, [], [])
        self.assertTrue(os.path.exists('test.db'))

        loaded_tasks = database.load_tasks('test.db')
        self.assertEqual(3, len(loaded_tasks))
        self.assertListEqual(new_tasks, loaded_tasks)

        # update some tasks
        updated_tasks = [
            {'remote_id': 4242, 'todoist_item_id': 'abaca222', 'title': 'task #2', 'kind': 'gitlab',
             'status': 'in_progress'},
        ]
        database.save_tasks('test.db', [], updated_tasks, [])
        self.assertTrue(os.path.exists('test.db'))

        loaded_tasks = database.load_tasks('test.db')
        self.assertEqual(3, len(loaded_tasks))
        self.assertListEqual([
            {'remote_id': 1414, 'todoist_item_id': 'abaca111', 'title': 'task #1', 'kind': 'gitlab', 'status': 'todo'},
            {'remote_id': 4242, 'todoist_item_id': 'abaca222', 'title': 'task #2', 'kind': 'gitlab',
             'status': 'in_progress'},
            {'remote_id': 2727, 'todoist_item_id': 'abaca222', 'title': 'task #3', 'kind': 'github', 'status': 'todo'},
        ], loaded_tasks)

        # close some tasks
        closed_tasks = [
            {'remote_id': 1414, 'todoist_item_id': 'abaca111', 'title': 'task #1', 'kind': 'gitlab', 'status': 'todo'},
        ]
        database.save_tasks('test.db', [], [], closed_tasks)
        self.assertTrue(os.path.exists('test.db'))

        loaded_tasks = database.load_tasks('test.db')
        self.assertEqual(2, len(loaded_tasks))
        self.assertListEqual([
            {'remote_id': 4242, 'todoist_item_id': 'abaca222', 'title': 'task #2', 'kind': 'gitlab',
             'status': 'in_progress'},
            {'remote_id': 2727, 'todoist_item_id': 'abaca222', 'title': 'task #3', 'kind': 'github', 'status': 'todo'},
        ], loaded_tasks)

        os.remove('test.db')

        pass


if __name__ == '__main__':
    unittest.main()
