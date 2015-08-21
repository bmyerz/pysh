import subprocess
import re
import os

__env_pat = re.compile('[$]([a-zA-Z0-9_]+)')


def __resolve_env_var(match):
    return str(os.environ[match.group(1)])


def pysh(cmd):
    c = re.sub(__env_pat, __resolve_env_var, cmd)
    subprocess.check_call(c, shell=True)
