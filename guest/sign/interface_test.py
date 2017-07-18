# -*- coding: utf-8 -*-

"""
    pyguest.interface_test
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Author: Y.Z.Y
    
"""

import requests
import unittest


class GetEventListTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        auth_user = ('admin', '1qaz1234')
        r = requests.get(self.url, auth=auth_user, params={'eid': ''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], "parameter error")

if __name__ == '__main__':
    unittest.main()
