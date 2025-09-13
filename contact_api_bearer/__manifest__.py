{
    "name": "Contact Creation API (Bearer Auth)",
    "version": "18.0.1.0.0",
    "category": "Controller",
    "summary": "Create contacts securely using Bearer Token authentication",
    "description": """
This module provides a secure API endpoint for creating contacts in Odoo 
using Bearer Token authentication.  

Features:
- REST API endpoint `/create/contact`
- Bearer token authentication
- Duplicate check by email or mobile
- Returns contact details on success
- Error handling for missing fields & duplicates
    """,
    "author": "Muhammed Aslam",
    "maintainers": ["Muhammed Aslam"],
    "contributors": ["Muhammed Aslam"],
    "website": "https://www.linkedin.com/in/muhammed-aslam-817327106/",
    "license": "LGPL-3",
    "depends": ["contacts"],
    "data": [],
    "installable": True,
    "application": False,
}