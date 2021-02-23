import os
import sqlite3


def load_tasks(where: str) -> list[dict]:
    """
    Load tasks from the database
    :param where the emplacement of the database
    :return: Loaded tasks
    """

    if not os.path.exists(where):
        create_database(where)

    conn = sqlite3.connect(where)

    tasks = []

    for entry in conn.execute("SELECT * FROM tasks"):
        tasks.append({
            'remote_id': entry[0],
            'todoist_item_id': entry[1]
        })

    return tasks


def save_tasks(where: str, tasks: list[dict]):
    """
    Save given tasks to the database
    :param where the emplacement of the database
    :param tasks the tasks to save
    """

    if not os.path.exists(where):
        create_database(where)

    with sqlite3.connect(where) as conn:
        for task in tasks:
            conn.execute("INSERT INTO tasks (remote_id, todoist_item_id) VALUES (?, ?)",
                         (task['remote_id'], task['todoist_item_id']))
            conn.commit()


def create_database(where: str):
    """
    Create the database & their definitions
    """

    with sqlite3.connect(where) as conn:
        conn.execute("CREATE TABLE tasks (remote_id integer, todoist_item_id text)")
        conn.commit()
