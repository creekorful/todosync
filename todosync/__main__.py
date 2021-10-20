#!/usr/bin/env python3
import click

from todosync import todosync


@click.command()
@click.option('--dry-run', is_flag=True, help='Do not commit the changes.')
@click.option('--config-dir', help='Override path to the config directory')
def execute(dry_run: bool, config_dir: str):
    """Synchronize issues & tasks from different sources into Todoist."""
    todosync.synchronize(dry_run, config_dir)


if __name__ == '__main__':
    execute()
