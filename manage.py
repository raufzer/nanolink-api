#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.wsgi import get_wsgi_application



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nanolink.settings')
    application = get_wsgi_application() 
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


def main():
    from django.core.management import execute_from_command_line

    if __name__ == "__main__":
        execute_from_command_line(["manage.py", "runserver", "0.0.0.0", "8080"])

if __name__ == "__main__":
    main()
    

