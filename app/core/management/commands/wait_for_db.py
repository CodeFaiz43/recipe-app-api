""" Django Command to wait for db to avialable"""
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError #"""django throws error when db is not ready"""
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django cmd to wait for db""" 
    def handle(self, *args, **option): 
        """Entry point Command"""
        self.stdout.write('Waiting For Database ...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OpError, OperationalError):
                self.stdout.write('Database Unavailable, Waiting 1 Second......')
                time.sleep(1) #sleep for 1 second
                
        self.stdout.write(self.style.SUCCESS('Database is Available !!!'))