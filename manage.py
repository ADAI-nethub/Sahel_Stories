#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv  # ✅ correct import

def main():
    """Run administrative tasks."""
    # Load .env file from project root if it exists
    env_path = Path(__file__).resolve().parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)

    # Default Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sahel_api.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate your virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
