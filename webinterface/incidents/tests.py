from django.test import TestCase
import unittest
from django.test import Client
from .models import Incidents

#Tests if the number of queries in Django database is equal to 2 
#(this number can be changed depending on expected number of queries)
class NumberTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
    
    def testNumber(self):
        list = len(Incidents.objects.all())
        self.assertEqual(list,2)

#A test to determine if log in of a student was successful
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.client.login(username = "Koketso", password = "mlkkok002")
    def testLogIn(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)