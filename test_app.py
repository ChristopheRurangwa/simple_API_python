from unittest import TestCase

from _pytest import unittest

from app import app
import getFunctionalities as Func


class Test(TestCase):
    """check if the response is ok; 200"""

    def test_check_response_status(self):
        tester = app.test_client(self)
        respon = tester.get('/api/ping')
        statuscode = respon.status_code
        self.assertEqual(statuscode, 200)

    '''checks if the data return is json type, if not, it is asserted that it is false'''

    def test_check_response_data(self):
        tester = app.test_client(self)
        respon = tester.get('/api/ping')
        data='{"success": True}'
        self.assertFalse(bytes(data.encode()) in respon.data)

    '''checks the content of the request'''

    def test_check_content_type_response(self):
        tester = app.test_client(self)
        respon = tester.get('/api/ping')
        self.assertEqual(respon.content_type, "application/json")

    '''testing response if it is of status 200'''

    def test_return_requstd_status_info(self):
        tester = app.test_client(self)
        respon = tester.get('/api/posts')
        statuscode = respon.status_code
        self.assertEqual(statuscode, 200)

    '''checks the content of the request'''

    def test_returned_content_type_info(self):
        tester = app.test_client(self)
        respon = tester.get('/api/posts')
        self.assertEqual(respon.content_type, "text/html; charset=utf-8")

    '''checks and confirms the data returned'''

    def test_returns_data_info(self):
        tester = app.test_client(self)
        respon = tester.get('/api/posts')
        self.assertTrue(bytes(Func.GetData.make_req('science', 'reads', 'asc').encode()) in respon.data)


if __name__ == '__main__':
    unittest.main()
