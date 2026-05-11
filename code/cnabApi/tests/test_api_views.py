import requests
from django.test import TestCase, Client
from django.urls import reverse
from django.urls import reverse_lazy
from cnab.models.importation import Document
from cnab.models.documentation import Documentation
from cnab.models.tipos import Type
from django.test.client import RequestFactory
from cnab.views.uploadfilesview import *
from model_mommy import mommy
from django.http.request import HttpRequest
from django.contrib import messages
from cnabApi.views import *
from django.core.exceptions import ValidationError


class APIViewTestClass(TestCase):
    def setUp(self):
        self.doc = mommy.make('Documentation')
        self.client = Client()

    def test_api(self):
        response = self.client.get(f'/api/names/{str(self.doc.dono)}/')
        self.assertEqual(response.status_code, 200)

class APIViewTestClass2(TestCase):
    def setUp(self):
        self.doc = mommy.make('Documentation')
        self.client = Client()

    def test_api2(self):
        response = self.client.get(f'/api/donos/{self.doc.id}/')
        self.assertEqual(response.status_code, 401)
