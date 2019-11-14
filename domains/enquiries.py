from datetime import datetime
import pytz

from ..auth import Auth


enquiries = {
    "pagination": True,
    "sorting": True,
    "authentication": Auth,
    "allowed_read_roles": ["admin", "root","consumer"],  # GET, OPTIONS
    "allowed_write_roles": ["admin", "root","consumer"],  # POST, PUT, DELETE
    "allowed_item_read_roles": ["admin", "root","consumer"],  # GET, OPTIONS
    "allowed_item_write_roles": ["admin", "root","consumer"],  # POST, PUT, DELETE
    "schema": {
        "user_id": {
            "type": "objectid",
            "required": True,
            "data_relation": {
                "resource": "consumers",
                "field": "_id",
                "embeddable": True,
            },
        },
        "phone_number": {"type": "string", "regex": r"^([0-9].{7,})$"},
        "topic": {"type": "string", "required": True},
        "messages": {
            "type": "list",
            "schema": {
                "type": "dict",
                "schema": {
                    "message": {"type": "string", "required": True},
                    "image": {"type": "string"},
                    "seen": {"type": "boolean", "default": False},
                    "timestamp": {
                        "type": "datetime",
                        "readonly": True,
                        "default": datetime.utcnow().replace(tzinfo=pytz.UTC),
                    },
                    "answered_by": {
                        "type": "objectid",
                        "readonly": True,
                        "data_relation": {
                            "resource": "admins",
                            "field": "_id",
                            "embeddable": True,
                        },
                    },
                },
            },
            "required": True,
        },
    },
}
