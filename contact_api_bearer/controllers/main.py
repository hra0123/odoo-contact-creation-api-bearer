from odoo import http
from odoo.http import request

class ContactAPI(http.Controller):

    @http.route("/create/contact", type="json", auth="bearer", methods=["POST"], csrf=False)
    def create_contact(self, **kw):
        data = {}
        try:
            user = request.env.user
            if not user or user._is_public():
                res_data = {
                    "status": "fail",
                    "message": "Authentication failed. Invalid or missing API key.",
                    "statusCode": 401,
                }
                return res_data
            data = request.httprequest.get_json()
            params = data.get("params", {})

            # Validate required fields
            required_fields = ["name", "mobile", "email"]
            missing_fields = [field for field in required_fields if not params.get(field)]
            if missing_fields:
                res_data = {
                    "statusCode": 400,
                    "statusDescription": "Missing required fields",
                    "error": f"Missing: {', '.join(missing_fields)}",
                }

            # Optional: check duplicates by email or mobile

            existing = request.env["res.partner"].sudo().search([
                "|",
                ("email", "=", params.get("email")),
                ("mobile", "=", params.get("mobile")),
            ], limit=1)

            if existing:
                return {
                    "status": "error",
                    "message": "Contact with same email or mobile already exists",
                    "contact_id": existing.id,
                }

            # Create new contact
            contact = request.env["res.partner"].sudo().create({
                "name": params.get("name"),
                "mobile": params.get("mobile"),
                "email": params.get("email"),
            })

            return {
                "status": "success",
                "contact_id": contact.id,
                "contact_name": contact.name,
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
            }
