"""
Django command to wait for the database to be available.
"""
from django.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        pass