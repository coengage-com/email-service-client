from typing import List

import requests  # type: ignore
import requests_toolbelt  # type: ignore

import settings
from email_service_client.client.types import CreateEmailIdentityPayload, EmailIdentity

API_BASE_URL = f"{settings.EMAIL_SERVICE_API_HOST}/api/v1"


class APIResource:
    def __init__(self, session: requests.Session) -> None:
        self._session = session
        self._session.hooks = {"response": lambda r, *args, **kwargs: r.raise_for_status()}


class _EmailIdentity(APIResource):
    resource_url: str

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)
        self.resource_url = f"{API_BASE_URL}/email-identities"

    def list(self) -> List[EmailIdentity]:
        return self._session.get(self.resource_url).json()

    def get(self, id: int) -> EmailIdentity:
        return self._session.get(f"{self.resource_url}/{id}").json()

    def create(self, data: CreateEmailIdentityPayload) -> dict:

        encoded_data = requests_toolbelt.MultipartEncoder(fields=data)
        self._session.post(
            self.resource_url,
            data=encoded_data,
            headers={"Content-Type": encoded_data.content_type},
        )
        return self._session.post(self.resource_url).json()

    def configure_sending(self, id: int) -> dict:
        return self._session.post(f"{self.resource_url}/{id}/configure/sending").json()

    def deconfigure_sending(self, id: int) -> dict:
        return self._session.post(f"{self.resource_url}/{id}/deconfigure/sending").json()

    def delete(self, id: int) -> dict:
        return self._session.post(f"{self.resource_url}/{id}/delete").json()

    def get_sending_dns_records(self, id: int) -> dict:
        return self._session.get(f"{self.resource_url}/{id}/dns-records/sending").json()

    def get_sending_verification_status(self, id: int) -> dict:
        return self._session.get(f"{self.resource_url}/{id}/verification-status/sending").json()
