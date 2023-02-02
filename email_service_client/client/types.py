from typing import TypedDict


class CreateEmailIdentityPayload(TypedDict):
    identity: str
    mail_from_subdomain: str


class EmailIdentity(TypedDict):
    id: int
    identity: str
    identity_type: str
    mail_from_subdomain: str
