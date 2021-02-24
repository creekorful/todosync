#!/usr/bin/env python3
import click

from todosync import todosync


@click.command()
@click.option('--dry-run', is_flag=True, help='Do not commit the changes.')
def execute(dry_run):
    """Synchronize your Gitlab issues with Todoist."""
    todosync.synchronize(dry_run)


if __name__ == '__main__':
    execute()
