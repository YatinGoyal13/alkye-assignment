import unittest
from task5 import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)  # 200 OK

    def test_get_user(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)  # 200 OK

    def test_get_nonexistent_user(self):
        response = self.app.get('/users/100')
        self.assertEqual(response.status_code, 404)  # 404 Not Found

    def test_create_user(self):
        data = {'name': 'John'}
        response = self.app.post('/users', json=data)
        self.assertEqual(response.status_code, 201)  # 201 Created

    def test_update_user(self):
        data = {'name': 'Updated Name'}
        response = self.app.put('/users/1', json=data)
        self.assertEqual(response.status_code, 200)  # 200 OK

    def test_update_nonexistent_user(self):
        data = {'name': 'Updated Name'}
        response = self.app.put('/users/100', json=data)
        self.assertEqual(response.status_code, 404)  # 404 Not Found

    def test_delete_user(self):
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)  # 204 No Content


if __name__ == '__main__':
    unittest.main()
