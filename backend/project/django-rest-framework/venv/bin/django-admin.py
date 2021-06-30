#!/Users/djsull93/new_work/drf-docker/project/django-rest-framework/venv/bin/python
# When the django-mywork.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-mywork.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-mywork instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-mywork.py is deprecated in favor of django-mywork.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
