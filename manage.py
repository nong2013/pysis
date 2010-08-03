#!/usr/bin/env python

import sys
from os.path import abspath, dirname, join
from django.core.management import setup_environ, execute_from_command_line

try:
    from settings import settings
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

# setup the environment before we start accessing things in the settings.
setup_environ(settings)

sys.path.insert(0, settings.PROJECT_PARENT)
sys.path.insert(0, settings.PROJECT_ROOT)
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

if __name__ == "__main__":
    execute_from_command_line()
