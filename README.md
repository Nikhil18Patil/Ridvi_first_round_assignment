**CREATED CRUD API according to assignment** 




###  GET AND POST EXample for Invoices
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


### 2. POST:
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

## Testing

The Invoice API is thoroughly tested using pytest. The test suite covers CRUD (Create, Read, Update, Delete) operations for invoices and their associated details. Key aspects of the testing include:

- **Creation**: Validating the correct creation of invoices with associated details.
- **Retrieval**: Ensuring accurate retrieval of invoice data.
- **Update**: Verifying the proper update of invoice details.
- **Deletion**: Confirming the correct deletion of invoices.

The test cases are designed to handle various scenarios, including edge cases and error conditions, to guarantee the robustness and reliability of the API. To run the tests locally, make sure to set up the necessary dependencies and use the following command:

```bash
pytest

