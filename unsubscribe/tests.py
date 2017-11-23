from django.utils import unittest
from django.test.client import RequestFactory
from django.contrib.auth.decorators import login_required
from django.test.client import Client
from clients.models import ClientProfile
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from views import *

class UnsubscribeTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    @login_required()
    def unsubscribe_test(self):
        request = RequestFactory().post(
            'unsubscribe/client_profile_id', {'email':'test@gmail.com'}
        )