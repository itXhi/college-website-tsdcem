from django.test import TestCase
from django.urls import reverse


class HomePageVideoTests(TestCase):
    def test_home_page_uses_absolute_static_video_url(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/static/videos/entry_video.mp4')
