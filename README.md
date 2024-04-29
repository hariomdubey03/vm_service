# Vendor Management System

## Installation
```
git clone https://github.com/hariomdubey03/vm_service.git
cd vm_service
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Operations/Vendor

## Create Vendor

POST /api/vendors/

### Add Vendor

This endpoint allows the client to add a new vendor to the system.

**Request Body**

- `name` (string, required): The name of the vendor.
- `contact_details` (string, required): Contact details of the vendor.
- `address` (string, required): Address of the vendor.
- `vendor_code` (string, required): Unique code for the vendor.
- `on_time_delivery_rate` (number, required): Rate of on-time delivery.
- `quality_rating_avg` (number, required): Average quality rating.
- `average_response_time` (number, required): Average response time of the vendor.
- `fulfillment_rate` (number, required): Fulfillment rate of the vendor.
    

**Response**

```
{
    "message": "Vendor created successfully",
    "data": {
        "id": 6,
        "name": "ABC Distributors",
        "contact_details": "info@abcdistributors.com",
        "address": "123 Main Street, Town, Country",
        "vendor_code": "V13579",
        "on_time_delivery_rate": 95.6,
        "quality_rating_avg": 4.5,
        "average_response_time": 3.1,
        "fulfillment_rate": 96.8
    }
}

 ```

> Body Parameters

```json
{
  "name": "DistributorA",
  "contact_details": "info@abcdistributors.com",
  "address": "123 Main Street, Town, Country",
  "vendor_code": "V13580",
  "on_time_delivery_rate": 95.6,
  "quality_rating_avg": 4.5,
  "average_response_time": 3.1,
  "fulfillment_rate": 96.8
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |none|
|» contact_details|body|string| yes |none|
|» address|body|string| yes |none|
|» vendor_code|body|string| yes |none|
|» on_time_delivery_rate|body|number| yes |none|
|» quality_rating_avg|body|number| yes |none|
|» average_response_time|body|number| yes |none|
|» fulfillment_rate|body|number| yes |none|

> Response Examples

> Create Vendor

```json
{
  "message": "Vendor created successfully",
  "data": {
    "id": 6,
    "name": "ABC Distributors",
    "contact_details": "info@abcdistributors.com",
    "address": "123 Main Street, Town, Country",
    "vendor_code": "V13579",
    "on_time_delivery_rate": 95.6,
    "quality_rating_avg": 4.5,
    "average_response_time": 3.1,
    "fulfillment_rate": 96.8
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Create Vendor|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» id|integer|true|none||none|
|»» name|string|true|none||none|
|»» contact_details|string|true|none||none|
|»» address|string|true|none||none|
|»» vendor_code|string|true|none||none|
|»» on_time_delivery_rate|number|true|none||none|
|»» quality_rating_avg|number|true|none||none|
|»» average_response_time|number|true|none||none|
|»» fulfillment_rate|number|true|none||none|

## Vendor Performance

GET /api/vendors/{vendor_id}/performance

The endpoint retrieves the performance data for a specific vendor with ID.

**Response**

``` json
{
    "message": "Performance metric data found",
    "data": {
        "vendor_id": 6,
        "on_time_delivery_rate": 50,
        "quality_rating_avg": 3,
        "average_response_time": 5400,
        "fulfillment_rate": 100
    }
}

 ```

> Body Parameters

```json
{}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> Vendor Performance

```json
{
  "message": "Performance metric data found",
  "data": {
    "vendor_id": 6,
    "on_time_delivery_rate": 50,
    "quality_rating_avg": 3,
    "average_response_time": 5400,
    "fulfillment_rate": 100
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Vendor Performance|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» vendor_id|integer|true|none||none|
|»» on_time_delivery_rate|integer|true|none||none|
|»» quality_rating_avg|integer|true|none||none|
|»» average_response_time|integer|true|none||none|
|»» fulfillment_rate|integer|true|none||none|

## Fetch Vendors

### GET /api/vendors/{vendor_id}/

This endpoint retrieves information about a specific vendor with the ID or for all the vendors if vendor_id not provided.

#### Request

No request body is required for this endpoint.

#### Response

The response will be a JSON object with the following schema:

``` json
{
    "message": "Vendor data found",
    "data": [
        {
            "id": 6,
            "name": "ABC Distributors",
            "contact_details": "info@abcdistributors.com",
            "address": "123 Main Street, Town, Country",
            "vendor_code": "V13579",
            "on_time_delivery_rate": 95.6,
            "quality_rating_avg": 4.5,
            "average_response_time": 3.1,
            "fulfillment_rate": 96.8
        }
    ]
}
or 
{
    "message": "Vendor data found",
    "data": [
        {
            "id": 6,
            "name": "ABC Distributors",
            "contact_details": "info@abcdistributors.com",
            "address": "123 Main Street, Town, Country",
            "vendor_code": "V13579",
            "on_time_delivery_rate": 95.6,
            "quality_rating_avg": 4.5,
            "average_response_time": 3.1,
            "fulfillment_rate": 96.8
        }
    ]
}

 ```

> Response Examples

> Fetch Vendors - All

```json
{
  "message": "Vendor data found",
  "data": [
    {
      "id": 6,
      "name": "ABC Distributors",
      "contact_details": "info@abcdistributors.com",
      "address": "123 Main Street, Town, Country",
      "vendor_code": "V13579",
      "on_time_delivery_rate": 95.6,
      "quality_rating_avg": 4.5,
      "average_response_time": 3.1,
      "fulfillment_rate": 96.8
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Fetch Vendors - All|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|[object]|true|none||none|
|»» id|integer|false|none||none|
|»» name|string|false|none||none|
|»» contact_details|string|false|none||none|
|»» address|string|false|none||none|
|»» vendor_code|string|false|none||none|
|»» on_time_delivery_rate|number|false|none||none|
|»» quality_rating_avg|number|false|none||none|
|»» average_response_time|number|false|none||none|
|»» fulfillment_rate|number|false|none||none|

## Update Vendor

PUT /api/vendors/{vendor_id}/

### Update Vendor Details

This endpoint allows the client to update the details of a specific vendor.

#### Request Body

- `name` (string, optional): The name of the vendor.
- `contact_details` (string, optional): Contact details of the vendor.
- `address` (string, optional): Address of the vendor.
- `vendor_code` (string, optional): Vendor code for identification.
- `on_time_delivery_rate` (number, optional): Rate of on-time delivery.
- `quality_rating_avg` (number, optional): Average quality rating.
- `average_response_time` (number, optional): Average response time.
- `fulfillment_rate` (number, optional): Rate of fulfillment.
    

#### Response

The response will be a JSON object with the following schema:

``` json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number"
                },
                "name": {
                    "type": "string"
                },
                "contact_details": {
                    "type": "string"
                },
                "address": {
                    "type": "string"
                },
                "vendor_code": {
                    "type": "string"
                },
                "on_time_delivery_rate": {
                    "type": "number"
                },
                "quality_rating_avg": {
                    "type": "number"
                },
                "average_response_time": {
                    "type": "number"
                },
                "fulfillment_rate": {
                    "type": "number"
                }
            }
        }
    }
}

 ```

> Body Parameters

```json
{
  "name": "ABC Distributors",
  "contact_details": "info@abcdistributors.com",
  "address": "Updated address",
  "vendor_code": "V13579",
  "on_time_delivery_rate": 95.6,
  "quality_rating_avg": 4.5,
  "average_response_time": 3.1,
  "fulfillment_rate": 96.8
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» name|body|string| yes |none|
|» contact_details|body|string| yes |none|
|» address|body|string| yes |none|
|» vendor_code|body|string| yes |none|
|» on_time_delivery_rate|body|number| yes |none|
|» quality_rating_avg|body|number| yes |none|
|» average_response_time|body|number| yes |none|
|» fulfillment_rate|body|number| yes |none|

> Response Examples

> Update Vendor

```json
{
  "message": "Vendor updated successfully",
  "data": {
    "id": 6,
    "name": "ABC Distributors",
    "contact_details": "info@abcdistributors.com",
    "address": "Updated address",
    "vendor_code": "V13579",
    "on_time_delivery_rate": 95.6,
    "quality_rating_avg": 4.5,
    "average_response_time": 3.1,
    "fulfillment_rate": 96.8
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Update Vendor|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» id|integer|true|none||none|
|»» name|string|true|none||none|
|»» contact_details|string|true|none||none|
|»» address|string|true|none||none|
|»» vendor_code|string|true|none||none|
|»» on_time_delivery_rate|number|true|none||none|
|»» quality_rating_avg|number|true|none||none|
|»» average_response_time|number|true|none||none|
|»» fulfillment_rate|number|true|none||none|

## Delete Vendor

DELETE /api/vendors/{vendor_id}/

### Delete Vendor

Deletes a specific vendor from the system.

#### Request Body

This request does not require a request body.

#### Response

- `message` (string, required): A message indicating the outcome of the request.
- `data` (null): This field will be null for a successful deletion.
    

#### JSON Schema

``` json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "data": {
            "type": "null"
        }
    },
    "required": ["message", "data"]
}

 ```

> Response Examples

> Delete Vendor

```json
{
  "message": "Vendor deleted successfully",
  "data": null
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Delete Vendor|Inline|

### Responses Data Schema

HTTP Status Code **204**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|null|true|none||none|

# Operations/Purchase Order

## Create Purchase Order

POST /api/purchase_orders/

The endpoint makes an HTTP POST request to create a new purchase order.

**Request Body**

- po_number (string, required): The unique purchase order number.
    
- vendor (number, required):The ID of the vendor associated with the purchase order.
    
- order_date (string, required): The date and time when the purchase order was created.
    
- expected_delivery_date (string, required): The expected delivery date of the items in the purchase order.
    
- items (array, required):
    
    - name (string): The name of the first item.
        
    - quantity (number): The quantity of the first item.
        
    - unit_price (number): The unit price of the first item.
        
    - name (string): The name of the second item.
        
    - quantity (number): The quantity of the second item.
        
    - unit_price (number): The unit price of the second item.
        
- quantity (number, required): The total quantity of all items in the purchase order.
    
- status (string, required): The status of the purchase order.
    
- quality_rating (number): The quality rating associated with the purchase order (if available).
    
- issue_date (string, required): The date and time when the purchase order was issued.
    
- acknowledgment_date (string): null - The date and time when the purchase order was acknowledged (if available).

> Body Parameters

```json
{
  "po_number": "PO6",
  "vendor": 6,
  "order_date": "2024-04-28 08:00:00.000000",
  "expected_delivery_date": "2024-05-05 08:00:00.000000",
  "items": [
    {
      "name": "Item 1",
      "quantity": 10,
      "unit_price": 20
    },
    {
      "name": "Item 2",
      "quantity": 5,
      "unit_price": 15
    }
  ],
  "quantity": 15,
  "status": "pending",
  "quality_rating": null,
  "issue_date": "2024-04-28 08:00:00.000000",
  "acknowledgment_date": null,
  "deleted_on": null
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» po_number|body|string| yes |none|
|» vendor|body|integer| yes |none|
|» order_date|body|string| yes |none|
|» expected_delivery_date|body|string| yes |none|
|» items|body|[object]| yes |none|
|»» name|body|string| yes |none|
|»» quantity|body|integer| yes |none|
|»» unit_price|body|integer| yes |none|
|» quantity|body|integer| yes |none|
|» status|body|string| yes |none|
|» quality_rating|body|null| yes |none|
|» issue_date|body|string| yes |none|
|» acknowledgment_date|body|null| yes |none|
|» deleted_on|body|null| yes |none|

> Response Examples

> Create Purchase Order

```json
{
  "message": "Purchase order created successfully",
  "data": {
    "id": 10,
    "po_number": "PO6",
    "vendor_id": 6,
    "order_date": "2024-04-28 08:00:00.000000",
    "expected_delivery_date": "2024-05-05 08:00:00.000000",
    "actual_delivery_date": null,
    "items": [
      {
        "name": "Item 1",
        "quantity": 10,
        "unit_price": 20
      },
      {
        "name": "Item 2",
        "quantity": 5,
        "unit_price": 15
      }
    ],
    "quantity": 15,
    "status": "pending",
    "quality_rating": null,
    "issue_date": "2024-04-28 08:00:00.000000",
    "acknowledgment_date": null
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Create Purchase Order|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» id|integer|true|none||none|
|»» po_number|string|true|none||none|
|»» vendor_id|integer|true|none||none|
|»» order_date|string|true|none||none|
|»» expected_delivery_date|string|true|none||none|
|»» actual_delivery_date|null|true|none||none|
|»» items|[object]|true|none||none|
|»»» name|string|true|none||none|
|»»» quantity|integer|true|none||none|
|»»» unit_price|integer|true|none||none|
|»» quantity|integer|true|none||none|
|»» status|string|true|none||none|
|»» quality_rating|null|true|none||none|
|»» issue_date|string|true|none||none|
|»» acknowledgment_date|null|true|none||none|

## POST Acknowledge Purchase Order

POST /api/purchase_orders/{po_id}/acknowledge/

This endpoint is used to acknowledge a purchase order with the specified ID.

#### Request Body

- acknowledgment_date (string, required): The date of acknowledgment.
    

#### Response

The response for this request is in JSON format and follows the schema below:

``` json
{
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "data": {
            "type": "null"
        }
    }
}

 ```

The response includes a message field with a string value and a data field with a null value.

> Body Parameters

```json
{
  "acknowledgment_date": "2024-04-28 10:00:00.000000"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» acknowledgment_date|body|string| yes |none|

> Response Examples

> Acknowledge Purchase Order

```json
{
  "message": "Purchase order acknowledged successfully",
  "data": null
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Acknowledge Purchase Order|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|null|true|none||none|

## Fetch Purchase Order

GET /api/purchase_orders/{po_id}/

### Retrieve Purchase Order Details

This endpoint retrieves the details of a specific purchase order by making a GET request to the specified URL.

#### Request
No request body is required for this request.

- URL parameter:
  - `id` (integer): The unique identifier of the purchase order to be retrieved.

#### Response
The response will be a JSON object with the following schema:

```json
{
  "message": "string",
  "data": {
    "id": "integer",
    "po_number": "string",
    "vendor_id": "integer",
    "order_date": "string",
    "expected_delivery_date": "string",
    "actual_delivery_date": "string",
    "items": [
      {
        "name": "string",
        "quantity": "integer",
        "unit_price": "integer"
      }
    ],
    "quantity": "integer",
    "status": "string",
    "quality_rating": "integer",
    "issue_date": "string",
    "acknowledgment_date": "string"
  }
}
```
The `data` object contains the details of the purchase order, including its unique identifier, purchase order number, vendor ID, order date, expected delivery date, actual delivery date, items included in the order, quantity, status, quality rating, issue date, and acknowledgment date.

#### Example
```json
{
  "message": "",
  "data": {
    "id": 0,
    "po_number": "",
    "vendor_id": 0,
    "order_date": "",
    "expected_delivery_date": "",
    "actual_delivery_date": null,
    "items": [
      {
        "name": "",
        "quantity": 0,
        "unit_price": 0
      }
    ],
    "quantity": 0,
    "status": "",
    "quality_rating": null,
    "issue_date": "",
    "acknowledgment_date": ""
  }
}
```

> Response Examples

> Fetch Purchase Order - All

```json
{
  "message": "Purchase orders found",
  "data": [
    {
      "id": 10,
      "po_number": "PO6",
      "vendor_id": 6,
      "order_date": "2024-04-28T13:30:00+05:30",
      "expected_delivery_date": "2024-05-05T13:30:00+05:30",
      "actual_delivery_date": null,
      "items": [
        {
          "name": "Item 1",
          "quantity": 10,
          "unit_price": 20
        },
        {
          "name": "Item 2",
          "quantity": 5,
          "unit_price": 15
        }
      ],
      "quantity": 15,
      "status": "pending",
      "quality_rating": null,
      "issue_date": "2024-04-28T13:30:00+05:30",
      "acknowledgment_date": "2024-04-28T15:30:00+05:30"
    }
  ]
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Fetch Purchase Order - All|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|[object]|true|none||none|
|»» id|integer|false|none||none|
|»» po_number|string|false|none||none|
|»» vendor_id|integer|false|none||none|
|»» order_date|string|false|none||none|
|»» expected_delivery_date|string|false|none||none|
|»» actual_delivery_date|null|false|none||none|
|»» items|[object]|false|none||none|
|»»» name|string|true|none||none|
|»»» quantity|integer|true|none||none|
|»»» unit_price|integer|true|none||none|
|»» quantity|integer|false|none||none|
|»» status|string|false|none||none|
|»» quality_rating|null|false|none||none|
|»» issue_date|string|false|none||none|
|»» acknowledgment_date|string|false|none||none|

## Delete Purchase Order

DELETE /api/purchase_orders/{po_id}/

This endpoint is used to delete a specific purchase order.

#### Request Body

This request does not require a request body.

#### Response

- Content-Type: application/json
- Schema:
    
    ``` json
      {
        "type": "object",
        "properties": {
          "message": {
            "type": "string"
          },
          "data": {
            "type": "null"
          }
        }
      }
    
     ```
    
- Description: This endpoint returns a JSON response with a message field and a data field. The message field contains a string value, and the data field is set to null.

> Body Parameters

```json
{}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|

> Response Examples

> Delete Purchase Order

```json
{
  "message": "Purchase order deleted successfully",
  "data": null
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Delete Purchase Order|Inline|

### Responses Data Schema

HTTP Status Code **204**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|null|true|none||none|

## Update Purchase Order

PUT /api/purchase_orders/11/

This endpoint allows the client to update a specific purchase order by sending an HTTP PUT request to the specified URL.

#### Request Body

- po_number (string): The unique purchase order number.
    
- vendor (number):The ID of the vendor associated with the purchase order.
    
- order_date (string): The date and time when the purchase order was created.
    
- expected_delivery_date (string): The expected delivery date of the items in the purchase order.
    
- items (array):
    
    - name (string): The name of the first item.
        
    - quantity (number): The quantity of the first item.
        
    - unit_price (number): The unit price of the first item.
        
    - name (string): The name of the second item.
        
    - quantity (number): The quantity of the second item.
        
    - unit_price (number): The unit price of the second item.
        
- quantity (number): The total quantity of all items in the purchase order.
    
- status (string): The status of the purchase order.
    
- quality_rating (number): The quality rating associated with the purchase order (if available).
    
- issue_date (string): The date and time when the purchase order was issued.
    
- acknowledgment_date (string): null - The date and time when the purchase order was acknowledged (if available).
    

#### Response

The response will be a JSON object with the following schema:

``` json
{
  "message": "string",
  "data": {
    "id": "integer",
    "po_number": "string",
    "vendor_id": "integer",
    "order_date": "string",
    "expected_delivery_date": "string",
    "actual_delivery_date": "string",
    "items": [
      {
        "name": "string",
        "quantity": "integer",
        "unit_price": "integer"
      }
    ],
    "quantity": "integer",
    "status": "string",
    "quality_rating": "integer",
    "issue_date": "string",
    "acknowledgment_date": "string"
  }
}

 ```

The `message` field provides additional information about the status of the request, while the `data` field contains the updated purchase order details.

> Body Parameters

```json
{
  "po_number": "PO7",
  "vendor": 6,
  "quality_rating": 4,
  "status": "completed"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» po_number|body|string| yes |none|
|» vendor|body|integer| yes |none|
|» quality_rating|body|integer| yes |none|
|» status|body|string| yes |none|

> Response Examples

> Update Purchase Order

```json
{
  "message": "Purchase order updated successfully",
  "data": {
    "id": 10,
    "po_number": "PO6",
    "vendor_id": 6,
    "order_date": "2024-04-28T13:30:00+05:30",
    "expected_delivery_date": "2024-05-05T13:30:00+05:30",
    "actual_delivery_date": "2024-04-29T05:51:39.400055",
    "items": [
      {
        "name": "Item 1",
        "quantity": 10,
        "unit_price": 20
      },
      {
        "name": "Item 2",
        "quantity": 5,
        "unit_price": 15
      }
    ],
    "quantity": 15,
    "status": "completed",
    "quality_rating": null,
    "issue_date": "2024-04-28T13:30:00+05:30",
    "acknowledgment_date": "2024-04-28T15:30:00+05:30"
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Update Purchase Order|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» id|integer|true|none||none|
|»» po_number|string|true|none||none|
|»» vendor_id|integer|true|none||none|
|»» order_date|string|true|none||none|
|»» expected_delivery_date|string|true|none||none|
|»» actual_delivery_date|string|true|none||none|
|»» items|[object]|true|none||none|
|»»» name|string|true|none||none|
|»»» quantity|integer|true|none||none|
|»»» unit_price|integer|true|none||none|
|»» quantity|integer|true|none||none|
|»» status|string|true|none||none|
|»» quality_rating|null|true|none||none|
|»» issue_date|string|true|none||none|
|»» acknowledgment_date|string|true|none||none|

# Auth

## authorize

POST /auth/api/authorize

This endpoint is used to authorize access to the API. The HTTP POST request should be made to /auth/api/authorize with a payload in raw request body type containing the platform_code.

### Request Body

- platform_code (string, required): The platform code for authorization.
    

### Response

The response for this request is a JSON object with the following schema:

``` json
{
  "message": "string",
  "data": {
    "access_token": "string",
    "refresh_token": "string"
  }
}

 ```

> Body Parameters

```json
{
  "platform_code": "8a650aae-cf0d-4a47-90e5-bbe7b0a6d9a9"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» platform_code|body|string| yes |none|

> Response Examples

> authorize

```json
{
  "message": "Access granted",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiOGE2NTBhYWUtY2YwZC00YTQ3LTkwZTUtYmJlN2IwYTZkOWE5IiwiZXhwIjoxNzE0MzYyMzAwLCJpYXQiOjE3MTQzNjA1MDB9._nB0A0QvFMPJgiPf3RkxwxZRwyaGY7Qpip80Obv01RU",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiOGE2NTBhYWUtY2YwZC00YTQ3LTkwZTUtYmJlN2IwYTZkOWE5IiwiZXhwIjoxNzE0MzY0MTAwLCJpYXQiOjE3MTQzNjA1MDB9.Ot8zYQpfTGCZ16JsudR_yJWzso5pPmteFYxymPkvBW4"
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|authorize|Inline|

### Responses Data Schema

HTTP Status Code **200**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» access_token|string|true|none||none|
|»» refresh_token|string|true|none||none|

## Regenerate-token

POST /auth/api/regenerate-token

This endpoint is used to regenerate a new access token using a refresh token.

#### Request

- Method: POST
- URL: `/auth/api/regenerate-token`
    
- Body:
    - refresh_token (string, required): The refresh token used to regenerate the access token.

#### Response

The response for this request will be a JSON object with the following properties:

``` json
{
  "message": "string",
  "data": {
    "access_token": "string",
    "refresh_token": "string"
  }
}

 ```

The `message` property may contain additional information about the response, while the `data` object will contain the regenerated `access_token` and `refresh_token`.

> Body Parameters

```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiOGE2NTBhYWUtY2YwZC00YTQ3LTkwZTUtYmJlN2IwYTZkOWE5IiwiZXhwIjoxNzE0MzY4NzYzLCJpYXQiOjE3MTQzNjUxNjN9.4AE12HJGfYzbvF_8576XavYvHqy8THrx_C6VWAqhe3c"
}
```

### Params

|Name|Location|Type|Required|Description|
|---|---|---|---|---|
|body|body|object| no |none|
|» refresh_token|body|string| yes |none|

> Response Examples

> regenerate-token

```json
{
  "message": "Token regenerated successfully",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiOGE2NTBhYWUtY2YwZC00YTQ3LTkwZTUtYmJlN2IwYTZkOWE5IiwiZXhwIjoxNzE0MzY2OTc3LCJpYXQiOjE3MTQzNjUxNzd9.m3sBtK5_OGJVNHWU1Hw5jJcqQ9ZOvYwhkkZC7trvHF0",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybV9jb2RlIjoiOGE2NTBhYWUtY2YwZC00YTQ3LTkwZTUtYmJlN2IwYTZkOWE5IiwiZXhwIjoxNzE0MzY4Nzc3LCJpYXQiOjE3MTQzNjUxNzd9.fhibdFo3uLSb9oUIDkEKlvH8hlxJ6uYGiwS8_ZzGOGQ"
  }
}
```

### Responses

|HTTP Status Code |Meaning|Description|Data schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|regenerate-token|Inline|

### Responses Data Schema

HTTP Status Code **201**

|Name|Type|Required|Restrictions|Title|description|
|---|---|---|---|---|---|
|» message|string|true|none||none|
|» data|object|true|none||none|
|»» access_token|string|true|none||none|
|»» refresh_token|string|true|none||none|

