import requests  # type: ignore
from requests import auth

from email_service_client.client.resources import _EmailIdentity, _OutgoingEmailRequest


class EmailServiceClient:
    def __init__(self, username: str, password: str):
        session = requests.Session()
        session.auth = auth.HTTPBasicAuth(username=username, password=password)
        self._email_identity = _EmailIdentity(session=session)
        self._outgoing_email_request = _OutgoingEmailRequest(session=session)

    @property
    def EmailIdentity(self):
        return self._email_identity

    @property
    def OutgoingEmailRequest(self):
        return self._outgoing_email_request
