from ..auth import Auth


crops = {
    "pagination": True,
    "sorting": True,
    "authentication": Auth,
    "allowed_read_roles": ["admin", "root","consumer"],  # GET, OPTIONS
    "allowed_write_roles": ["admin","root"],  # POST, PUT, DELETE
    "allowed_item_read_roles": ["admin", "root","consumer"],  # GET, OPTIONS
    "allowed_item_write_roles": ["admin","root"],  # POST, PUT, DELETE
    "public_methods": ["GET"],
    "public_item_methods": ["GET"],
    "schema": {
        "name": {
            "type": "dict",
            "schema": {
                "en": {"type": "string", "required": True, "default": ""},
                "mm": {"type": "string", "required": True, "default": ""},
            },
        },
        "image": {"type": "string", "required": True},
        "details": {
            "type": "dict",
            "schema": {
                "en": {"type": "string", "required": True, "default": ""},
                "mm": {"type": "string", "required": True, "default": ""},
            },
        },
    },
}
