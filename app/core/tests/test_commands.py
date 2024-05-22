""" Test custom django management cmds """
from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase

# mocking db behaviour

@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Test Commands """
    
    def test_wait_for_db_ready(self, patched_check):
        """ Test waiting for database if db is ready... """
        #whenever patched_check is called we are returing true
        patched_check_return_value=True
        #call code inside wait_for_db
        call_command('wait_for_db')
        #calling 
        patched_check.assert_called_once_with(databases=['default'])
        
    #sleep method before we check with db again
    @patch('time.sleep')
    #check if db is not ready we delay and try again
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """test waiting for db when getting operational error"""
        patched_check.side_effect = [Psycopg2Error] * 2 +  [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])