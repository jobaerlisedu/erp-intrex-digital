from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
import json

class DocumentationAJAXTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testadmin'
        self.password = 'password123'
        # Skip creating if already exists
        if not User.objects.filter(username=self.username).exists():
            self.user = User.objects.create_superuser(
                username=self.username,
                email='testadmin@example.com',
                password=self.password
            )

    def test_docs_standard_request(self):
        self.client.login(username=self.username, password=self.password)
        # Request docs index normally
        response = self.client.get(reverse('docs_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'erp/documentation.html')
        self.assertContains(response, 'docs-container')

    def test_docs_ajax_request(self):
        self.client.login(username=self.username, password=self.password)
        # Request docs index via AJAX
        response = self.client.get(
            reverse('docs_index'),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')
        data = json.loads(response.content)
        self.assertIn('html_content', data)
        self.assertIn('current_path', data)
        self.assertEqual(data['current_path'], 'index.md')
