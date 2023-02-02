from unittest import TestCase
from unittest.mock import patch

import settings

API_HOST_URL = f"{settings.EMAIL_SERVICE_API_HOST}"


class ResourceTestCase(TestCase):
    def setUp(self) -> None:
        self.requests_get_patch = patch("requests.Session.get").start()
        self.requests_post_patch = patch("requests.Session.post").start()

    def tearDown(self) -> None:
        self.requests_get_patch.stop()
        self.requests_post_patch.stop()
