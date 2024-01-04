**CREATED CRUD API according to assignment** 

### 1. Retrieve a List of Invoices
**Endpoint**: `/invoices/`
**Method**: `GET`
**Example**:
```bash
http GET https://your-api-base-url.com/invoices/
**Response**
[
  {
    "id": 1,
    "date": "2022-01-31",
    "customer_name": "John Doe",
    "invoice_details": [
      {
        "id": 1,
        "description": "Product A",
        "quantity": 3,
        "unit_price": 10.99,
        "price": 32.97
      }
    ]
  },
  
]

**GET**:(specific by id)
http GET https://your-api-base-url.com/invoices/1/

**RESPONSE**
{
    "id": 1,
    "date": "2022-01-31",
    "customer_name": "John Doe",
    "invoice_details": [
      {
        "id": 1,
        "description": "Product A",
        "quantity": 3,
        "unit_price": 10.99,
        "price": 32.97
      }
    ]
  }



**### 2. POST:**
**Create a New Invoice**
Endpoint: /invoices/
Method: POST
Example:
base_url = "https://your-api-base-url.com"
endpoint = "/invoices/"

payload = {
    "date": "2022-01-31",
    "customer_name": "John Doe",
    "invoice_details": [
        {
            "description": "Product A",
            "quantity": 3,
            "unit_price": 10.99,
            "price": 32.97
        }
    ]
}

response = requests.post(f"{base_url}{endpoint}", json=payload)

**RESPONSE:**
{
    "date": "2022-01-31",
    "customer_name": "John Doe",
    "invoice_details": [
        {
            "description": "Product A",
            "quantity": 3,
            "unit_price": 10.99,
            "price": 32.97
        }
    ]
}


