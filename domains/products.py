from ..auth import Auth


products = {
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
        "engine_power": {"type": "float", "required": True},
        "horse_power": {"type": "float", "required": True},
        "category": {
            "type": "objectid",
            "data_relation": {
                "resource": "categories",
                "field": "_id",
                "embeddable": True,
            },
            "required": True,
        },
        "crop_type": {
            "type": "list",
            "schema": {
                "type": "objectid",
                "data_relation": {
                    "resource": "crops",
                    "field": "_id",
                    "embeddable": True,
                },
                "required": True,
            },
        },
        "specifications": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "en": {
                        "type": "dict",
                        "schema": {
                            "key": {"type": "string", "required": True},
                            "value": {"type": "string", "required": True},
                        },
                    },
                    "mm": {
                        "type": "dict",
                        "schema": {
                            "key": {"type": "string", "required": True},
                            "value": {"type": "string", "required": True},
                        },
                    },
                },
            },
        },
        "features": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "en": {
                        "type": "dict",
                        "schema": {
                            "key": {"type": "string", "required": True},
                            "value": {"type": "string", "required": True},
                        },
                    },
                    "mm": {
                        "type": "dict",
                        "schema": {
                            "key": {"type": "string", "required": True},
                            "value": {"type": "string", "required": True},
                        },
                    },
                },
            },
        },
    },
}
