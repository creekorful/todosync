#!/usr/bin/env python3
import click

from todosync import todosync


@click.command()
@click.option('--dry-run', is_flag=True, help='Do not commit the changes.')
@click.option('--config', help='Path to the configuration file.')
def execute(dry_run: bool, config: str):
    """Synchronize your Git{hub,lab} issues with Todoist."""
    todosync.synchronize(dry_run, config)


if __name__ == '__main__':
    execute()
