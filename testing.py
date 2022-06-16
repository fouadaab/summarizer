import json
import unittest
from models.db_model import DBManipulation

from api import app
# set our application to testing mode
app.testing = True

class TestApi(unittest.TestCase):

    def test_main(self):
        with app.test_client() as client:
            
            _id = DBManipulation.get_new_id()

            # send data as POST form to endpoint
            sent = {'data': 'Sentence 1. Sentence 2. Sentence 3.'}
            result = client.post(
                '/text',
                data=sent
            )

            # check result from server with expected data
            self.assertEqual(
                result.data,
                f'{{"_id":{_id}}}\n'.encode()
            )
    
    # TODO: Increase Test Coverage...