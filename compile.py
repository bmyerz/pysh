import sys
import stat
import os

if __name__ == "__main__":
    infn = sys.argv[1]
    base, ext = os.path.splitext(infn)

    if ext != '.py':
        raise ValueError("Can only compile py files; given {}".format(ext))

    script_name = "{}".format(base)
    muscle_name = "_{}.py".format(base)

    with open(script_name, 'w') as outf:
        outf.writelines(['#! /usr/bin/env python\n',
                         'import macropy.activate\n',
                         'import _{}\n'.format(base)])

    os.chmod(script_name, os.stat(script_name).st_mode | stat.S_IEXEC)

    with open(muscle_name, 'w') as outf:
        outf.writelines(['from macropy.string_interp import macros, s\n'])
        with open(infn, 'r') as inf:
            outf.write(inf.read())


