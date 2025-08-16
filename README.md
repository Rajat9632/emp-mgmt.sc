# Employee Management System

A comprehensive Django-based employee management system with REST API endpoints for managing employees and attendance records.

## Features

- **Employee Management**: CRUD operations for employee records
- **Attendance Tracking**: Record and manage employee attendance
- **REST API**: Full REST API with authentication
- **Swagger Documentation**: Interactive API documentation
- **Token Authentication**: Secure API access with token-based authentication
- **Filtering & Pagination**: Advanced filtering and pagination support

## Tech Stack

- **Backend**: Django 4.2.7
- **API Framework**: Django REST Framework
- **Database**: PostgreSQL (configurable)
- **Authentication**: Token Authentication
- **Documentation**: Swagger/OpenAPI
- **Testing**: Built-in Django testing framework

## Installation & Setup

### Prerequisites

- Python 3.8+
- PostgreSQL (or SQLite for development)
- Virtual environment (recommended)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd employee_mgmt
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the root directory:
   ```bash
   # Database Configuration
   DATABASE_URL=postgresql://username:password@localhost:5432/employee_db
   
   # Django Settings
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   
   # Optional: For production
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Seed Sample Data** (Optional)
   ```bash
   python manage.py seed_data
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- http://127.0.0.1:8000/swagger/
- this is open to the swagger
- POST  /api-token-auth/ will the auth token by entering the username and password of the superuser which will u create 

- In the top-right corner of the swagger there is an swagger button click on that there u need too enter the auth token like this 
-   Token your_auth_token
-  this is my auth_token if u want u can directly use it
-   90cb5ca9afb9b1942619872cea5e5f89ff7c9290

### Employees
- `GET /api/employees/` - List all employees
- `POST /api/employees/` - Create new employee
- `GET /api/employees/{id}/` - Get employee details
- `PUT /api/employees/{id}/` - Update employee
- `DELETE /api/employees/{id}/` - Delete employee

### Attendance
- `GET /api/attendance/` - List all attendance records
- `POST /api/attendance/` - Create attendance record
- `GET /api/attendance/{id}/` - Get attendance details
- `PUT /api/attendance/{id}/` - Update attendance
- `DELETE /api/attendance/{id}/` - Delete attendance

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/swagger/
- **ReDoc**: http://localhost:8000/redoc/

## Models

### Employee
- `id` (AutoField): Unique identifier
- `first_name` (CharField): Employee's first name
- `last_name` (CharField): Employee's last name
- `email` (EmailField): Unique email address
- `phone_number` (CharField): Contact number
- `department` (CharField): Department name
- `position` (CharField): Job position
- `hire_date` (DateField): Date of hiring
- `salary` (DecimalField): Employee salary
- `is_active` (BooleanField): Active status

### Attendance
- `id` (AutoField): Unique identifier
- `employee` (ForeignKey): Linked employee
- `date` (DateField): Attendance date
- `check_in` (TimeField): Check-in time
- `check_out` (TimeField): Check-out time
- `status` (CharField): Attendance status (Present/Absent/Late/Leave)

### Charts
- http://127.0.0.1:8000/api/charts/
-this above link includes pie and bar charts for employees for departments and attendance respectively.


I tried to deploy it on vercel but currently i can't, will try in future. Thankyou