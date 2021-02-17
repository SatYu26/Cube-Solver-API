#!"e:\projects\flutter practice\cube\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'rubik-solver==0.2.0','console_scripts','rubik_solver'
__requires__ = 'rubik-solver==0.2.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rubik-solver==0.2.0', 'console_scripts', 'rubik_solver')()
    )
