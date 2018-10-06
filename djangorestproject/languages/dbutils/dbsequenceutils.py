"""
DB Sequence Utils with SequenceUtils class containing all required sequence related utilities
funciton.
"""

from django.apps import apps
from django.db import models, router, connection
import os
from pathlib import Path

PROJDIR = Path(__file__).parents[2]
PROJNAME = "djangorestproject"


class SequenceUtils(object):

    def __init__(self):
        self.connection = connection

    def sequencelist(self):
        """Returns a list of information about all DB sequences for all models in all apps."""

        sequence_list = []
        try:
            assert os.environ.get("DJANGO_SETTINGS_MODULE"), "No DJANGO_SETTINGS_MODULE variable defined"
        except AssertionError as aerr:
            raise aerr

        for app_config in apps.get_app_configs():
            for model in router.get_migratable_models(app_config, self.connection.alias):
                if not model._meta.managed:
                    continue
                if model._meta.swapped:
                    continue
                for f in model._meta.local_fields:
                    if isinstance(f, models.AutoField):
                        sequence_list.append({'table': model._meta.db_table, 'column': f.column})
                        break  # Only one AutoField is allowed per model, so don't bother continuing.

                for f in model._meta.local_many_to_many:
                    # If this is an m2m using an intermediate table,
                    # we don't need to reset the sequence.
                    if f.rel.through is None:
                        sequence_list.append({'table': f.m2m_db_table(), 'column': None})

        return sequence_list


if __name__ == "__main__":
    sl = SequenceUtils()
    print(sl.sequencelist())
