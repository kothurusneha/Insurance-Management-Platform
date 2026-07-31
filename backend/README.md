# Insurance Management Platform

## Project Description

The Insurance Management Platform is a Flask-based backend application designed to manage insurance-related operations efficiently. The system provides secure user authentication, customer management, policy management, payment tracking, claim processing, document management, and dashboard reporting.

The application uses RESTful APIs with JWT-based authentication to ensure secure access to protected resources.

---

## Technologies Used

* Python
* Flask
* MySQL
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Flask-Bcrypt
* Flask-Migrate
* SQLAlchemy
* PyMySQL
* Thunder Client (API Testing)

---

## Features Implemented

### Authentication Module

* User Registration
* User Login
* Password Hashing using Bcrypt
* JWT Token Authentication
* Protected API Access

### Customer Management

* Add new customers
* View customer details

### Policy Management

* Create insurance policies
* View policy details

### Payment Management

* Add payment records
* View payment details

### Claim Management

* Submit claims
* View claim records

### Document Management

* Upload customer documents
* View uploaded documents

### Report Dashboard

* View overall system statistics:

  * Total Customers
  * Total Policies
  * Total Claims
  * Total Payments

---

## Project Structure

```
Insurance-Management-Platform

backend
│
├── app.py
├── extensions.py
├── requirements.txt
│
├── models
│   ├── user.py
│   ├── customer.py
│   ├── policy.py
│   ├── payment.py
│   ├── claim.py
│   └── document.py
│
└── routes
    ├── auth_routes.py
    ├── customer_routes.py
    ├── policy_routes.py
    ├── payment_routes.py
    ├── claim_routes.py
    ├── document_routes.py
    └── report_routes.py
```

---

## Database

Database Name:

```
insurance_db
```

Database Tables:

* users
* customers
* policies
* payments
* claims
* documents

---

## API Endpoints

### Authentication

#### Register User

```
POST /api/register
```

#### Login User

```
POST /api/login
```

---

### Customer APIs

#### Create Customer

```
POST /api/customers
```

#### Get Customers

```
GET /api/customers
```

---

### Policy APIs

#### Create Policy

```
POST /api/policies
```

#### Get Policies

```
GET /api/policies
```

---

### Payment APIs

#### Create Payment

```
POST /api/payments
```

#### Get Payments

```
GET /api/payments
```

---

### Claim APIs

#### Create Claim

```
POST /api/claims
```

#### Get Claims

```
GET /api/claims
```

---

### Document APIs

#### Upload Document

```
POST /api/documents
```

#### Get Documents

```
GET /api/documents
```

---

### Report API

#### Dashboard Report

```
GET /api/reports/dashboard
```

---

## Installation and Setup

### 1. Clone the Repository

```
git clone <repository-url>
```

### 2. Navigate to Backend Folder

```
cd backend
```

### 3. Create Virtual Environment

```
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

### 5. Install Dependencies

```
pip install -r requirements.txt
```

### 6. Configure Database

Update MySQL database details in `app.py`.

Example:

```
mysql+pymysql://username:password@localhost/insurance_db
```

### 7. Run Application

```
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

---

## API Testing

All APIs were tested using:

```
Thunder Client
```

JWT authentication was used for protected endpoints.

---

## Screenshots

The project screenshots are available in:

```
screenshots/
```

Included screenshots:

* Login Success
* Customer APIs
* Policy APIs
* Payment APIs
* Claim APIs
* Document APIs
* Report Dashboard

---

## Future Enhancements

* Frontend user interface
* Online premium payment integration
* Email notifications
* Advanced analytics dashboard
* Role-based permissions

---

## Conclusion

The Insurance Management Platform provides a secure and efficient solution for managing insurance operations. The system successfully implements authentication, customer management, policy handling, payment tracking, claim processing, document management, and reporting features using Flask and MySQL.
