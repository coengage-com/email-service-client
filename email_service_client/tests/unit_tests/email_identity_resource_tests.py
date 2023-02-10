from unittest.mock import MagicMock, patch

from email_service_client.client import EmailServiceClient
from email_service_client.client.constants import HOST
from email_service_client.tests.unit_tests.base import ResourceTestCase


class EmailIdentityResourceTests(ResourceTestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_list_email_identities(self):
        dummy_list = MagicMock(status_code=200)
        self.requests_get_patch.return_value = dummy_list
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(email_service_client.EmailIdentity.list(), dummy_list.json())
        self.requests_get_patch.assert_called_with(f"{HOST}/api/v1/email-identities")

    def test_get_email_identity(self):

        dummy_list = MagicMock(status_code=200)
        self.requests_get_patch.return_value = dummy_list
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(email_service_client.EmailIdentity.get(23434), dummy_list.json())
        self.requests_get_patch.assert_called_with(f"{HOST}/api/v1/email-identities/23434")

    @patch("requests_toolbelt.MultipartEncoder")
    def test_create_email_identity(self, multipart_encoder_patch):

        dummy_response = MagicMock(status_code=200)
        self.requests_post_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        encoded_data = multipart_encoder_patch(fields={"identity": "domain.com"})
        self.assertEqual(
            email_service_client.EmailIdentity.create(data={"identity": "domain.com"}),
            dummy_response.json(),
        )
        self.requests_post_patch.assert_called_with(
            f"{HOST}/api/v1/email-identities",
            data=encoded_data,
            headers={"Content-Type": encoded_data.content_type},
        )

    def test_configure_sending_email_identity(self):
        dummy_response = MagicMock(status_code=200)
        self.requests_post_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.EmailIdentity.configure_sending(id=19),
            dummy_response.json(),
        )
        self.requests_post_patch.assert_called_with(
            f"{HOST}/api/v1/email-identities/19/configure/sending"
        )

    def test_deconfigure_sending_email_identity(self):
        dummy_response = MagicMock(status_code=200)
        self.requests_post_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.EmailIdentity.deconfigure_sending(id=19),
            dummy_response.json(),
        )
        self.requests_post_patch.assert_called_with(
            f"{HOST}/api/v1/email-identities/19/deconfigure/sending"
        )

    def test_delete_sending_email_identity(self):
        dummy_response = MagicMock(status_code=200)
        self.requests_post_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.EmailIdentity.delete(id=19),
            dummy_response.json(),
        )
        self.requests_post_patch.assert_called_with(f"{HOST}/api/v1/email-identities/19/delete")

    def test_get_sending_dns_records(self):
        dummy_response = MagicMock(status_code=200)
        self.requests_get_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.EmailIdentity.get_sending_dns_records(id=19),
            dummy_response.json(),
        )
        self.requests_get_patch.assert_called_with(
            f"{HOST}/api/v1/email-identities/19/dns-records/sending"
        )

    def test_get_sending_verification_status(self):
        dummy_response = MagicMock(status_code=200)
        self.requests_get_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.EmailIdentity.get_sending_verification_status(id=19),
            dummy_response.json(),
        )
        self.requests_get_patch.assert_called_with(
            f"{HOST}/api/v1/email-identities/19/verification-status/sending"
        )
