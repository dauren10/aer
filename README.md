# Swagger with Django REST Framework

Django Swagger

## Getting Started

Works on **Python 3+** and **Django 3+**.

1. Install dependencies:

```
sudo docker-compose up --build
```

2. Run migrations & start the server:

```
fill .env file
sudo docker-compose run web python manage.py migrate
sudo docker-compose up
```

## Testing

Navigate below URL to view docs .

```
localhost:8000/api/v1/swagger/schema
Data POST to fill database from CSV file
```
