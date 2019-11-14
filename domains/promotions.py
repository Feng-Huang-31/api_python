from ..auth import Auth


promotions = {
    "pagination": True,
    "sorting": True,
    "authentication": Auth,
    "allowed_read_roles": ["admin", "consumer","root"],  # GET, OPTIONS
    "allowed_write_roles": ["admin","root"],  # POST, PUT, DELETE
    "allowed_item_read_roles": ["admin", "consumer","root"],  # GET, OPTIONS
    "allowed_item_write_roles": ["admin","root"],  # POST, PUT, DELETE
    "public_methods": ["GET"],
    "public_item_methods": ["GET"],
    "schema": {
        "title": {"type": "string", "default": ""},
        "image": {"type": "string", "required": True},
        "body": {"type": "string", "default": ""},
        "created_by": {
            "type": "objectid",
            "required": True,
            "data_relation": {"resource": "admins", "field": "_id", "embeddable": True},
        },
    },
}
