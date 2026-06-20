from django.test import TestCase


class HomePageTests(TestCase):
    def test_homepage_says_welcome(self):
        # Pretend to be a visitor going to the homepage
        response = self.client.get("/")

        # Check the door actually opened (no error)
        self.assertEqual(response.status_code, 200)

        # Check it said the right thing
        self.assertIn(b"Welcome to my Library API!", response.content)


class HealthCheckTests(TestCase):
    def test_health_says_ok(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})
