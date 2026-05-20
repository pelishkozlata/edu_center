# edu_center

Educational Center Management System built with Django and Django REST Framework.

The system allows educational centers to manage:
- branches
- students
- teachers
- groups
- lesson schedules
- attendance
- subscription plans

---

# Live Demo

Deployed project:

https://edu-center-jnpa.onrender.com/

Swagger API documentation:

https://edu-center-jnpa.onrender.com/api/docs/

---

# Technologies

## Backend
- Python
- Django
- Django REST Framework
- PostgreSQL

## Authentication
- JWT Authentication
- djangorestframework-simplejwt

## Documentation
- drf-spectacular (Swagger/OpenAPI)

## DevOps
- Docker
- Docker Compose
- Gunicorn
- WhiteNoise

---

# Setup Instructions

## 1. Clone the repository

```bash
git clone <repository-url>
cd edu_center
```

---

## 2. Create `.env` file

Example:

```env
DEBUG=True

SECRET_KEY=your_secret_key

DB_NAME=education_center
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## 3. Start the project

```bash
docker-compose up

If Docker images need to be rebuilt:

```bash
docker-compose up --build
``````

The project starts with Docker Compose according to the technical requirements.

---

## 4. Apply migrations

```bash
docker-compose exec backend python manage.py migrate
```

---

## 5. Create a superuser

```bash
docker-compose exec backend python manage.py createsuperuser
```

Enter the required phone number and password according to the custom user model fields.

---

## 6. Run tests

```bash
docker-compose exec backend pytest
```

---

# API Documentation

Swagger UI:

http://127.0.0.1:8000/api/docs/

Production Swagger:

https://edu-center-jnpa.onrender.com/api/docs/

OpenAPI schema:

http://127.0.0.1:8000/api/schema/


See also:
[API Endpoints](docs/api_endpoints.md)

---

# Authentication

The API uses JWT authentication.

Authorization header example:

```http
Authorization: Bearer <access_token>
```

The system uses access and refresh tokens.

Users authenticate using a phone number and password.

---

# ER Diagram

![ER Diagram](docs/er_diagram.png)

---

# Main Features

## Authentication & Authorization
- Custom user model with phone authentication
- JWT authentication
- Role-based permissions (ADMIN / TEACHER)

## Branch Management
- Create and archive branches
- Multi-branch support

## Subject Management
- Create and archive subjects
- Unique subject names within a branch

## Student Management
- Student profiles
- Parent/guardian contact information
- Search and filtering

## Group Management
- Add/remove students from groups
- Group lesson support

## Lesson Scheduling
- Individual lessons
- Group lessons
- Recurring lesson templates
- Lesson conflict detection

## Attendance
- Present/absent tracking
- Attendance history
- Teacher attendance marking

## Subscription Plans
- Pricing grids
- Subject-based subscriptions
- Individual and group pricing plans

## Reporting
- Teacher schedules
- Student attendance history
- Basic branch statistics

---

# Testing

Implemented tests include:
- authentication
- permissions
- lesson conflict detection
- attendance marking
- API endpoints

Run tests:

```bash
docker-compose exec backend pytest
```

---

# Environment Variables

| Variable | Description |
|---|---|
| SECRET_KEY | Django secret key |
| DEBUG | Debug mode |
| DB_NAME | PostgreSQL database name |
| DB_USER | PostgreSQL username |
| DB_PASSWORD | PostgreSQL password |
| DB_HOST | PostgreSQL host |
| DB_PORT | PostgreSQL port |
| ALLOWED_HOSTS | Allowed Django hosts |

---

# Technical Requirements Compliance

The project satisfies the required technical requirements:

- Django + Django REST Framework backend
- PostgreSQL database
- JWT authentication
- REST API
- Swagger/OpenAPI documentation
- Docker Compose support
- Project starts with `docker-compose up`
- Unit and API tests
- Role-based permissions
- Conflict prevention for lessons
- Attendance management
