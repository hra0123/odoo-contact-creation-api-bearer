# Contact Creation API (Bearer Auth) - Odoo 18

This Odoo module provides a secure REST API endpoint to create contacts using **Bearer Token authentication**.  
It validates input, prevents duplicates, and returns structured JSON responses.

---

## 🚀 Features
- JSON endpoint: `/create/contact`
- Authentication via **Bearer Token**
- Validates required fields (`name`, `mobile`, `email`)
- Prevents duplicate contacts (by email or mobile)
- Returns contact details on success
- Error handling for missing fields, duplicates, or invalid token

---

## 📦 Installation
1. Clone this repository into your Odoo addons path:
   ```bash
   git clone https://github.com/hra0123/odoo-contact-creation-api-bearer.git
   ```
2. Restart your Odoo service.
3. Activate developer mode in Odoo.
4. Install the **Contact Creation API** module from the Apps menu.

---

## 🔧 Usage

### Endpoint
`POST /create/contact`

### Headers
```
Authorization: Bearer <your_token>
Content-Type: application/json
```

### Example Request
```json
{
  "params": {
    "name": "John Doe",
    "mobile": "+971500000000",
    "email": "john.doe@example.com"
  }
}
```

### Example Success Response
```json
{
  "status": "success",
  "contact_id": 45,
  "contact_name": "John Doe"
}
```

### Example Error Response
```json
{
  "statusCode": 400,
  "statusDescription": "Missing required fields",
  "error": "Missing: email"
}
```

---

## 🛠 Dependencies
- Odoo 18.0
- `contacts` module

---

## 👨‍💻 Author
- **Muhammed Aslam**  
  [LinkedIn](https://www.linkedin.com/in/muhammed-aslam-817327106/)  

---

## 📜 License
This module is licensed under the **LGPL-3** license.
