from django.test import TestCase


# Create your tests here.
class HomePageTest(TestCase):

    def test_uses_home_template(self):
        # Gets the response from home page
        response = self.client.get('/')
        # Returns True if template used was correct one
        self.assertTemplateUsed(response, 'lists/home.html')
