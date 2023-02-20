from collections import namedtuple
from typing import TypedDict
from uuid import UUID

AttachmentDetails = namedtuple("AttachmentDetails", ["filename", "content", "mimetype"])


class CreateEmailIdentityPayload(TypedDict):
    identity: str
    mail_from_subdomain: str


class EmailIdentity(TypedDict):
    id: int
    identity: str
    identity_type: str
    mail_from_subdomain: str


class OutgoingEmailRequestPayload(TypedDict):
    from_name: str
    from_address: str
    recipients: list[str]
    cc: list[str]
    bcc: list[str]
    reply_to: list[str]
    subject: str
    body: str
    html: str
    amp: str
    source_uuid: UUID
    attachments: list[AttachmentDetails]


class OutgoingEmailRequestResponse(TypedDict):
    request_uuid: UUID
    status: str
    status_updated_at: str
