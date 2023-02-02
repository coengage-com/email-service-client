import requests  # type: ignore
import requests_toolbelt  # type: ignore

import settings
from client.types import CreateEmailIdentityPayload, EmailIdentity

API_BASE_URL = f"{settings.EMAIL_SERVICE_API_HOST}/api/v1"


class APIResource:
    def __init__(self, session: requests.Session) -> None:
        self._session = session


class _EmailIdentity(APIResource):
    resource_url: str

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)
        self.resource_url = f"{API_BASE_URL}/email-identities"

    def list(self) -> list[EmailIdentity]:
        return self._session.get(self.resource_url).json()

    def get(self, id) -> EmailIdentity:
        return self._session.get(f"{self.resource_url}/{id}").json()

    def create(self, data: CreateEmailIdentityPayload):
        encoded_data = requests_toolbelt.MultipartEncoder(fields=data)
        self._session.post(
            self.resource_url,
            data=encoded_data,
            headers={"Content-Type": encoded_data.content_type},
        )
        return self._session.post(f"{self.resource_url}").json()
