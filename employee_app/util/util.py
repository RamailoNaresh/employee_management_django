import uuid


def get_uuid_id(length = None):
    id = uuid.uuid4()
    if length:
        return id[:length]
    return id