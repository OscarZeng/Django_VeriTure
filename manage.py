#!/usr/bin/env python

import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_VeriTure.settings")

    from django.core.management import execute_from_command_line

    from certviewer import configure_app
    from certviewer.config import get_config
    if sys.argv == ["manage.py", "runserver"]:
        conf = get_config()
        print(conf)
        configure_app(conf)
    execute_from_command_line(sys.argv)
