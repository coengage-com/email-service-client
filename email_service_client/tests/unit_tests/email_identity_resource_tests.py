from unittest.mock import MagicMock, patch

from email_service_client.client import EmailServiceClient
from email_service_client.client.constants import HOST
from email_service_client.tests.unit_tests.base import ResourceTestCase


class EmailIdentityResourceTests(ResourceTestCase):
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


class OutgoingEmailRequestResourceTests(ResourceTestCase):
    @patch("requests_toolbelt.MultipartEncoder")
    def test_create(self, multipart_encoder_patch):

        dummy_response = MagicMock(status_code=200)
        self.requests_post_patch.return_value = dummy_response
        email_service_client = EmailServiceClient(username="dummy", password="dummy")
        self.assertEqual(
            email_service_client.OutgoingEmailRequest.create(
                data={
                    "from_name": "John",
                    "from_address": "john@coengagage.com",
                    "recipients": [("jane@plivo.com")],
                    "subject": "test",
                    "body": "hello!",
                    "amp": "",
                    "cc": [],
                    "bcc": [],
                    "reply_to": ["mridula@coengagedev.com"],
                    "html": "",
                    "source_uuid": None,
                    "attachments": [],
                }
            ),
            dummy_response.json(),
        )
        multipart_encoder_patch.assert_called_with(
            fields=[
                ("from_address", "john@coengagage.com"),
                ("recipients", "jane@plivo.com"),
                ("reply_to", "mridula@coengagedev.com"),
                ("subject", "test"),
                ("body", "hello!"),
            ]
        )
        self.requests_post_patch.assert_called_with(
            f"{HOST}/api/v1/outgoing-email-requests",
            data=multipart_encoder_patch(),
            headers={"Content-Type": multipart_encoder_patch().content_type},
        )
