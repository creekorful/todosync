import os
import sqlite3
from pathlib import Path


def load_tasks(where: Path) -> list[dict]:
    """
    Load tasks from the database
    :param where the emplacement of the database
    :return: Loaded tasks
    """

    if not os.path.exists(where):
        create_database(where)

    conn = sqlite3.connect(where)

    tasks = []

    for entry in conn.execute("SELECT remote_id, todoist_item_id, title, due_date, kind, status FROM tasks"):
        tasks.append({
            'remote_id': entry[0],
            'todoist_item_id': entry[1],
            'title': entry[2],
            'due_date': entry[3],
            'kind': entry[4],
            'status': entry[5],
        })

    return tasks


def save_tasks(where: Path, new_tasks: list[dict], updated_task: list[dict], closed_tasks: list[dict]):
    """
    Save given tasks to the database
    :param where the emplacement of the database
    :param new_tasks the newly added tasks
    :param updated_task the updated tasks
    :param closed_tasks the deleted tasks
    """

    if not os.path.exists(where):
        create_database(where)

    with sqlite3.connect(where) as conn:
        # create new tasks
        for task in new_tasks:
            conn.execute("""INSERT INTO tasks (
                remote_id,
                todoist_item_id,
                title,
                due_date,
                kind,
                status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (task['remote_id'], task['todoist_item_id'],
                  task['title'], task['due_date'],
                  task['kind'], task['status']))

        # update updated tasks
        for task in updated_task:
            conn.execute("""UPDATE tasks SET
                status = ?,
                title = ?,
                due_date = ?
                WHERE remote_id = ? AND kind = ?
            """, (task['status'], task['title'], task['due_date'], task['remote_id'], task['kind']))

        # delete closed tasks
        for task in closed_tasks:
            conn.execute("DELETE FROM tasks WHERE remote_id = ? AND kind = ?", (task['remote_id'], task['kind']))

        conn.commit()


def create_database(where: Path):
    """
    Create the tables
    """

    with sqlite3.connect(where) as conn:
        conn.execute("""CREATE TABLE tasks (
            remote_id integer,
            todoist_item_id text,
            title text,
            due_date text,
            kind text,
            status text
        )""")
        conn.commit()
