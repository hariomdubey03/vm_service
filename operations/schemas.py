# Schema for Vendor model
VENDOR_POST = {
    "name": {"type": "string", "maxlength": 255, "required": True},
    "contact_details": {"type": "string", "required": True},
    "address": {"type": "string", "required": True},
    "vendor_code": {
        "type": "string",
        "maxlength": 50,
        "required": True,
    },
    "on_time_delivery_rate": {"type": "float", "required": True},
    "quality_rating_avg": {"type": "float", "required": True},
    "average_response_time": {"type": "float", "required": True},
    "fulfillment_rate": {"type": "float", "required": True},
}
VENDOR_PUT = {
    "name": {"type": "string", "maxlength": 255},
    "contact_details": {"type": "string"},
    "address": {"type": "string"},
    "vendor_code": {"type": "string", "maxlength": 50},
    "on_time_delivery_rate": {"type": "float"},
    "quality_rating_avg": {"type": "float"},
    "average_response_time": {"type": "float"},
    "fulfillment_rate": {"type": "float"},
}

# Schema for PurchaseOrder model
PURCHASE_ORDER_POST = {
    "po_number": {"type": "string", "maxlength": 50, "required": True},
    "vendor": {"type": "integer", "required": True},
    "order_date": {"type": "string", "required": True},
    "expected_delivery_date": {"type": "string", "required": True},
    "actual_delivery_date": {"type": "string", "nullable": True},
    "items": {"type": "list", "required": True},
    "quantity": {"type": "integer", "required": True},
    "status": {"type": "string", "maxlength": 50, "required": True},
    "quality_rating": {"type": "float", "nullable": True},
    "issue_date": {"type": "string", "required": True},
    "acknowledgment_date": {"type": "string", "nullable": True},
}
PURCHASE_ORDER_PUT = {
    "po_number": {"type": "string", "maxlength": 50},
    "vendor": {"type": "integer"},
    "order_date": {"type": "string"},
    "expected_delivery_date": {"type": "string"},
    "actual_delivery_date": {"type": "string", "nullable": True},
    "items": {"type": "list"},
    "quantity": {"type": "integer"},
    "status": {"type": "string", "maxlength": 50},
    "quality_rating": {"type": "float", "nullable": True},
    "issue_date": {"type": "string"},
    "acknowledgment_date": {"type": "string", "nullable": True},
}
