from unittest.mock import MagicMock

from client import EmailServiceClient
from settings import EMAIL_SERVICE_API_HOST
from tests.unit_tests.base import ResourceTestCase


class EmailIdentityResourceTests(ResourceTestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_list_email_identities(self):
        dummy_list = MagicMock()
        self.requests_get_patch.return_value = dummy_list
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(email_service_client.EmailIdentity.list(), dummy_list.json())
        self.requests_get_patch.assert_called_with(
            f"{EMAIL_SERVICE_API_HOST}/api/v1/email-identities"
        )

    def test_get_email_identity(self):
        dummy_list = MagicMock()
        self.requests_get_patch.return_value = dummy_list
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(email_service_client.EmailIdentity.get(23434), dummy_list.json())
        self.requests_get_patch.assert_called_with(
            f"{EMAIL_SERVICE_API_HOST}/api/v1/email-identities/23434"
        )

    def test_create_email_identity(self):
        dummy_response = MagicMock()
        self.requests_post_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.EmailIdentity.create(data={"identity": "domain.com"}),
            dummy_response.json(),
        )
        self.requests_post_patch.assert_called_with(
            f"{EMAIL_SERVICE_API_HOST}/api/v1/email-identities"
        )
