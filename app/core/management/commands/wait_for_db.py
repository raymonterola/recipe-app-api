"""Django command to wait for database to be available."""

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db import OperationalError


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **kwargs):
        """Command entrypoint"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting a second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database Available!'))
