from django.test import TestCase, RequestFactory
from django.utils import timezone
from django.contrib.auth.models import AnonymousUser, User
from user.views import register, login
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user

class user_tests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='foo2', password='bar2')

    def test_logger(self):
        request = self.factory.get('/user/login/')
        request.user = self.user
        response = login(request)
        self.assertEqual(response.status_code, 200)

    def test_auth(self):
        self.assertFalse(get_user(self.client).is_authenticated())
        self.client.login(username='foo2',password='bar2')
        self.assertTrue(get_user(self.client).is_authenticated())

    def test_good_data(self):
        resp = self.client.get('/user/register/', {'username':'foo','password1':'bar','password2':'bar'})
        self.assertEqual(resp.status_code, 200)

        self.client.login(username='foo',password='bar')
        self.assertTrue(get_user(self.client).is_authenticated())

        # respond = self.client.get('/user/login/', {'username':'foo','password1':'bar','password2':'bar'})
        # self.assertEqual(resp.status_code, 200)
