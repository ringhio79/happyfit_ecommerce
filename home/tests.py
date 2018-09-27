from django.test import TestCase

# Create your tests here.
class TestDjango(TestCase):
        

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "home/home.html")