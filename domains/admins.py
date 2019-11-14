from ..auth import Auth


admins = {
    "pagination": False,
    "sorting": True,
    "authentication": Auth,
    "allowed_read_roles": ["admin", "root"],  # GET, OPTIONS
    "allowed_write_roles": ["admin", "root"],  # POST, PUT, DELETE
    "allowed_item_read_roles": ["admin", "root"],  # GET, OPTIONS
    "allowed_item_write_roles": ["admin", "root"],  # POST, PUT, DELETE
    "schema": {
        "name": {"type": "string", "required": True},
        "email": {
            "type": "string",
            "regex": r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
            "unique": True,
            "required": True,
        },
        "role": {"type": "string", "allowed": ["root", "admin"], "required": True},
        "password": {"type": "string", "required": True, "min": 8},
    },
}
