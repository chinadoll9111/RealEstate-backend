# Real Estate Backend Application

This is a Django REST Framework backend for a Real Estate application.  
It supports listing properties, filtering, search, user registration, login, inquiries, and JWT authentication.

---

## Features

1. **Listings**
   - View all listings: `/api/listings/`
   - Filter by category: `/api/listings/?category=SALE|RENT|BUY`
   - View single listing: `/api/listings/<id>/`
   - Only published and unsold listings are visible.

2. **Search**
   - Search by title or description: `/api/search/?search=query`

3. **User Registration & Login**
   - Register new user: `/api/register/`  
     Body:
     ```json
     {
       "username": "yourusername",
       "email": "youremail@example.com",
       "password": "yourpassword"
     }
     ```
   - Login (JWT token): `/api/login/`  
     Body:
     ```json
     {
       "username": "yourusername",
       "password": "yourpassword"
     }
     ```
     Response:
     ```json
     {
       "refresh": "refresh_token_here",
       "access": "access_token_here"
     }
     ```

4. **Inquiries**
   - Make inquiry about a listing: `/api/inquiry/`  
     Headers: `Authorization: Bearer <access_token>`  
     Body:
     ```json
     {
       "listing": 1,
       "message": "I am interested in this property"
     }
     ```

5. **Admin**
   - Access Django admin: `/admin/`
   - Manage users, listings, and inquiries.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/real-estate-backend.git
   cd real-estate-backend

2. Create a virtual environment:

   python -m venv venv
   source venv/Scripts/activate  # Windows
   source venv/bin/activate      # Linux/Mac

3. Install requirements:

   pip install -r requirements.txt

4. Apply migrations:

   python manage.py migrate

5. Create superuser (for admin):

   python manage.py createsuperuser

6. Run server:

   python manage.py runserver

7. Open browser:

   API: http://127.0.0.1:8000/api/
   Admin: http://127.0.0.1:8000/admin/

Notes

JWT token is required for making inquiries.
Use the access token from login in Authorization header as:
Bearer <access_token>