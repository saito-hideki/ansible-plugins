# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase

import psutil as ps


DOCUMENTATION = '''
    callback: cpu_usage
    callback_type: aggregate
    requirements:
        - psutil
    short_description: Add cpu usage to tasks and handlers
    version_added: "2.0"
    description:
        - Ansible callback plugin for profiling cpu usage
'''


def profiling(f=None):
    """
    Decorator that will run the function and print a line-by-line profile
    """
    def wrapper(*args, **kwargs):
        proc = ps.Process()
        val = f(*args, **kwargs)
        results = []
        cpu_user, cpu_system, _, _ = proc.cpu_times()
        print(
            "CPU Times: user({user:.8f}) system({system:.8f}) @{func}".format(
            user=cpu_user, system=cpu_system, func=f.__name__))
        return val

    return wrapper


class CallbackModule(CallbackBase):
    """
    This callback module tells you how long your plays ran for.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'memory_usage'
    CALLBACK_NEEDS_WHITELIST = True

    def __init__(self):
        super(CallbackModule, self).__init__()

    @profiling
    def v2_playbook_on_start(self, playbook):
        pass

    @profiling
    def v2_playbook_on_task_start(self, task, is_conditional):
        pass

    @profiling
    def v2_playbook_on_handler_task_start(self, task):
        pass

    @profiling
    def v2_playbook_on_include(self, included_file):
        pass

#
# [EOF]
#