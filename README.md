# Ansible Plugins

This project provides various plugins for Ansible.

## Callback Plugins

### memory_usage

#### Description

`memory_usage` plugin is using python memory_profiler modues and it shows memory usage information of each tasks.

#### Requirements

- memory-profiler==0.52.0

#### Installation

You can locate plugin file to `%PLAYBOOK DIR%/callback_plugins/memory_usage.py` and use it.

#### Configuration

```
[defaults]
callback_whitelist = memory_usage
```

#### Example output of Playbook

```
$ ansible-playbook -i inventory test.yml
MemoryUsage: 47.32812500 MiB @v2_playbook_on_start

PLAY [all] *****************************************************************************************

TASK [Gathering Facts] *****************************************************************************
MemoryUsage: 48.62890625 MiB @v2_playbook_on_task_start
ok: [127.0.0.1]

TASK [include_role] ********************************************************************************
MemoryUsage: 49.28125000 MiB @v2_playbook_on_task_start

TASK [test : ping] *********************************************************************************
MemoryUsage: 49.33203125 MiB @v2_playbook_on_task_start
ok: [127.0.0.1]

PLAY RECAP *****************************************************************************************
127.0.0.1                  : ok=2    changed=0    unreachable=0    failed=0
```
