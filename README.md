# Ansible Plugins

This project provides various plugins for Ansible.

## Callback Plugins

### memory_usage

#### Description

`memory_usage` plugin is using python memory_profiler modues and it shows memory usage information of each tasks.

#### Requirements

- psutil==5.4.5

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
Memory Usage: rss(46.4727)MiB vms(4237.7969)MiB pfaults(16557) pageins(0) @v2_playbook_on_start

PLAY [all] ******************************************************************************************

TASK [Gathering Facts] ******************************************************************************
Memory Usage: rss(47.8867)MiB vms(4242.8203)MiB pfaults(17095) pageins(0) @v2_playbook_on_task_start
ok: [127.0.0.1]

TASK [include_role] *********************************************************************************
Memory Usage: rss(48.2539)MiB vms(4243.0703)MiB pfaults(18763) pageins(0) @v2_playbook_on_task_start

TASK [test : ping] **********************************************************************************
Memory Usage: rss(48.3281)MiB vms(4243.0703)MiB pfaults(20443) pageins(0) @v2_playbook_on_task_start
ok: [127.0.0.1] => {"changed": false, "failed": false, "ping": "pong"}

PLAY RECAP ******************************************************************************************
127.0.0.1                  : ok=2    changed=0    unreachable=0    failed=0
```
