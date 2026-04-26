# edu_center

## Setup Instructions

### 1. Clone the repository

```
git clone <repository-url>
cd edu_center
```

### 2. Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate
```

### 3. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 4. Create a superuser

```
python manage.py createsuperuser
```
Enter the required phone number and password according to the custom user model fields.

### 5. Run the development server

```
python manage.py runserver
```

## ER Diagram
![ER Diagram](docs/er_diagram.png)

## API Documentation
See [API Endpoints](docs/api_endpoints.md)