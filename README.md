# Todosync

Synchronize issues & tasks from different sources into [Todoist](https://todoist.com).

## Supported sources

- [Github](https://github.com)
- [Gitlab](https://gitlab.com)
- [Debian BTS](https://bugs.debian.org)

Example config file:

```toml
[config]
gitlab_token = "" # the token to connect with Gitlab
github_token = "" # the token to connect with Github
todoist_token = "" # the token to connect with Todoist
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

[sources."https://bugs.debian.org/983289"]
labels = [0] # the optional labels to add to the tasks
default = 0 # default tasks section
todo = 0 # where we put tasks with todo status (section)
in_progress = 0 # where we put tasks with in_progress status (section)
```