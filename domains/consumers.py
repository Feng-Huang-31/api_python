from ..auth import Auth


consumers = {
    "pagination": False,
    "sorting": True,
    "authentication": Auth,
    "allowed_read_roles": ["admin","root"],  # GET, OPTIONS
    "allowed_write_roles": ["admin","root"],  # POST, PUT, DELETE
    "allowed_item_read_roles": ["admin","root", "consumer"],  # GET, OPTIONS
    "allowed_item_write_roles": ["admin", "root","consumer"],  # POST, PUT, DELETE
    "schema": {
        "full_name": {"type": "string", "required": True},
        "email": {
            "type": "string",
            "regex": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        },
        "phone_number": {
            "type": "string",
            "regex": r"^([0-9].{7,})$",
            "unique": True,
            "required": True,
        },
        "profile_image": {"type": "string", "default": ""},
        "notification_token": {"type": "list"},
        "gender": {"type": "string", "allowed": ["male", "female", "other"]},
        "address": {
            "type": "dict",
            "schema": {
                "division": {"type": "string", "required": True},
                "township": {"type": "string", "required": True},
                "village": {"type": "string"},
            },
        },
    },
}
