# 📝 Todo App

## Loyiha haqida (O‘zbekcha)

Bu FastAPI frameworkidan foydalangan holda yaratilgan oddiy Todo ilovasi bo‘lib, foydalanuvchiga vazifalar (todo) ro‘yxatini yaratish, o‘zgartirish, ko‘rish va o‘chirish imkonini beradi. Loyihada GET, POST, PUT, DELETE, JWT autentifikatsiyasi, login va register metodlari to‘liq ishlaydi.

### Texnologiyalar:
- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (migratsiya uchun)
- Pydantic (schema va validatsiya uchun)
- dotenv (maxfiy ma'lumotlar uchun)
- JWT (JSON Web Token) autentifikatsiyasi

### Faolliklar:
- Todo qo‘shish (POST /todos/)
- Barcha todolarni ko‘rish (GET /todos/)
- Bitta todoni yangilash (PUT /todos/{id})
- Bitta todoni o‘chirish (DELETE /todos/{id})
- Foydalanuvchini ro‘yxatdan o‘tkazish (POST /register)
- Foydalanuvchini tizimga kirish va JWT token olish (POST /login)

##Autentifikatsiya
- Loyihada JWT autentifikatsiyasi qo‘llaniladi.
- Foydalanuvchilar POST /register endpointi orqali ro‘yxatdan o‘ta oladi.
- Foydalanuvchilar POST /login orqali tizimga kirib, JWT token olishlari mumkin.
- JWT tokenini Authorization headerida Bearer sifatida yuborish kerak.
---

## About the Project (English)

This is a simple Todo application built using the FastAPI framework. The project allows users to create, update, view, and delete tasks (todos). It supports GET, POST, PUT, DELETE, JWT authentication, login, and register operations.

### Technologies used:
Python 3

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic (for database migration)
- Pydantic (for schema and validation)
- dotenv (for environment variables)
- JWT (JSON Web Token) authentication

### Features:
- Add a todo (`POST /todos/`)
- View all todos (`GET /todos/`)
- Update a todo (PUT /todos/{id})
- Delete a todo (DELETE /todos/{id})
- Register a user (POST /register)
- Login a user and receive a JWT token (POST /login)


## Authentication

- JWT authentication is used in this project.
- Users can register via the POST /register endpoint.
- Users can log in via the POST /login endpoint and receive a JWT token.
- The JWT token must be sent as a Bearer token in the Authorization header.




