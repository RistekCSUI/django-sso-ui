import json
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile


from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):
    def test_views(self):
        r = self.client.get("/login/")
        self.assertRedirects(r, "hello")
