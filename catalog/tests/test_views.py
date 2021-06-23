from django.test import TestCase
from django.urls import reverse

from catalog.models import Author

class AuthorCreateViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/author/create/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('author-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/author_form.html')

    def test_form_invalid_first_name(self):
        response = self.client.post(reverse('author-create'))
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')

    def test_form_invalid_last_name(self):
        response = self.client.post(reverse('author-create'), {'first_name': 'Tom'})
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'last_name', 'This field is required.')

    def test_redirect_to_author_detail_on_success(self):
        response = self.client.post(reverse('author-create'), {'first_name': 'Tom', 'last_name': 'Hack'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/catalog/author/1')







