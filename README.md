# Todosync

Synchronize your [Github](https://github.com) or [Gitlab](https://gitlab.com) issues with [Todoist](https://todoist.com).

Example config file:

```toml
[config]
gitlab_token = "" # the token to connect with Gitlab
github_token = "" # the token to connect with Github
todoist_token = "" # the token to connect with Todoist
database_file = "todosync.db" # where to save the local cache
default_labels = [0] # list of labels to apply on ALL tasks

[sources."https://gitlab.com/creekorful/test"]
labels = [0] # the optional labels to add to the tasks
default = 0 # default tasks section
todo = 0 # where we put tasks with todo status (section)
in_progress = 0 # where we put tasks with in_progress status (section)

[sources."https://github.com/creekorful/test"]
labels = [0] # the optional labels to add to the tasks
default = 0 # default tasks section
todo = 0 # where we put tasks with todo status (section)
in_progress = 0 # where we put tasks with in_progress status (section)
```