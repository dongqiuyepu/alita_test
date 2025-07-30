

import unittest
import requests
from app import app
import threading
import time

class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 5000, 'use_reloader': False})
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1)  # Give server time to start

    def test_hello_world(self):
        response = requests.get('http://localhost:5000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello, World!')

if __name__ == '__main__':
    unittest.main()

