from django.test import TestCase
from django.contrib.auth.models import User
from .models import SampleInformation
from django.contrib.auth import authenticate
# Create your tests here.

class TableViewsTestCase(TestCase):
    def test_display(self):
        resp=self.client.get('/display/')
        self.assertEqual(resp.status_code, 200)


#    def test_login(self):
#        resp1=self.client.get('/home/')
#        self.assertEqual(resp1.status_code, 302)
#        resp2=self.client.get('/display/')
#        self.assertEqual(resp2.status_code, 200)
#    def test_logout(self):
#        resp=self.client.get('/logout/')
#        self.assertEqual(resp.status_code, 200)

 #   def test_good_login(self):

#        sample_1= SampleInformation.objects.get(pk=1)
    def setUp(self):
        self.user=User.objects.create_user(username='jacob',email='jacob@email.com',password='password')
    def test_home(self):
        login_successful= self.client.login(username="jacob", password="password")
        if self.assertTrue(login_successful):
            resp=self.client.get('/home/')
            self.assertEqual(resp.status_code, 200)
        else:
            resp=self.client.get('/login/')
            self.assertEqual(resp.status_code, 200)
    def tearDown(self):
        self.user.delete()
#   def test_login_required(self):
