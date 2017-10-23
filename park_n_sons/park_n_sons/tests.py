from django.test import TestCase

class url_tests(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('login' in resp.content)
        self.assertTrue('register' in resp.content)
        self.assertFalse('Logout' in resp.content)

    def test_register(self):
        resp = self.client.get('/user/register/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('username' in resp.content)
        self.assertTrue('password' in resp.content)
        self.assertTrue('submit' in resp.content)
        self.assertTrue('Password confirmation' in resp.content)
        self.assertTrue('Your password must contain at least 8 characters' in resp.content)
        self.assertFalse('Logout' in resp.content)

    def test_login(self):
        resp = self.client.get('/user/login/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('username' in resp.content)
        self.assertTrue('password' in resp.content)
        self.assertTrue('login' in resp.content)
        self.assertFalse('Logout' in resp.content)

    def test_admin(self):
        resp = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('username' in resp.content)
        self.assertTrue('password' in resp.content)
        self.assertTrue('Django administration' in resp.content)
        self.assertFalse('Logout' in resp.content)

    def test_search(self):
        resp = self.client.get('/search/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('Free Activity' in resp.content)
        self.assertTrue('Accessible by Public Transport' in resp.content)
        self.assertTrue('Child Friendly' in resp.content)
        self.assertFalse('Login' in resp.content)
