# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.callback import CallbackBase
from memory_profiler import *

import sys


DOCUMENTATION = '''
    callback: memory_usage
    callback_type: aggregate
    requirements:
        - memory_profiler
    short_description: Add memory usage to tasks and handlers
    version_added: "2.0"
    description:
        - Ansible callback plugin for profiling memory usage
'''


def profiling(f=None):
    """
    Decorator that will run the function and print a line-by-line profile
    """
    def wrapper(*args, **kwargs):
        prof = LineProfiler(backend='psutil')
        val = prof(f)(*args, **kwargs)
        results = []
        for _, lines in prof.code_map.items():
            for _, mem_info in lines:
                results.append(mem_info)
        print(
            "MemoryUsage: {usage:.8f} MiB @{func}".format(
            usage=results[0][0], func=f.__name__))
        return val

    return wrapper


class CallbackModule(CallbackBase):
    """
    This callback module tells you how long your plays ran for.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'timer'
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