"""uc-automa metadata new-id: a fresh identifier for dc:identifier.

Every document, sidecar and decision record is identified by a random
UUID written as a URN, the value `uuidgen -r` was run by hand to make.
"""

import uuid


def new_id() -> str:
    """A random (version 4) UUID as a urn:uuid: value."""
    return uuid.uuid4().urn
