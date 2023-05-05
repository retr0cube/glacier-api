import unittest
import json

from api import api

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = api.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'\xf0\x9f\x91\x80 Curiosity kills the \xf0\x9f\x90\xb1 cat!')

    def test_get_package(self):
        response = self.app.get('/api/packages/mnl')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'monolith')
        self.assertEqual(data['slug_name'], 'mnl')

if __name__ == '__main__':
    unittest.main()
