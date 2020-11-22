from django.test import TestCase


class URLTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)


class URLTest2(TestCase):
    def test_homepage(self):
        response = self.client.get('/o-kompanii/')
        self.assertEqual(response.status_code, 200)


