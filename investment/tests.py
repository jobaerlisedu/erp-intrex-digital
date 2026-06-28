from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class InvestmentCRMTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test_admin", password="password123", is_superuser=True)
        self.client = Client()
        self.client.force_login(self.user)

    def test_investor_list_view(self):
        response = self.client.get(reverse('investment:investor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investment/investors.html')

    def test_payables_list_view(self):
        response = self.client.get(reverse('investment:payables_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'investment/payables.html')
        self.assertIn('schedules', response.context)


