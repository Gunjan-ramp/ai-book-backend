
# Library Management System - Backend

FastAPI backend for managing books with AI-powered insights using Mistral AI.

## Features
- CRUD operations for books
- Search by title/author
- AI-generated taglines using Mistral API
- MSSQL database integration
- RESTful API endpoints

## Prerequisites
- Python 3.9+
- MSSQL Server
- Mistral API key

## Setup

1. **Clone repository**
   ```bash
   git clone https://github.com/Gunjan-ramp/ai-book-backend
   cd backend

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Environment variables**

   Create .env file:

    ```bash 
    Server = your_sql_server
    Driver = ODBC+Driver+17+for+SQL+Server
    DataBaseBronze = your_db_name
    user = your_db_user
    Password = your_db_password
    MISTRAL_API_KEY = your_mistral_key

4. **Database setup**

    Create database matching your DataBaseBronze name

Tables will be auto-created on first run

5. **Running the Server**

   ```bash
   uvicorn main:app --reload

6. **API Documentation**
Access Swagger UI at http://localhost:8000/docs

7. **Endpoints**


| Method   | Endpoint                      | Description                   |
|----------|-------------------------------|-------------------------------|
| `POST`   | `/books`                      | Create new book               |
| `GET`    | `/books`                      | List all books                |
| `GET`    | `/books/{id}`                 | Get single book               |
| `PUT`    | `/books/{id}`                 | Update book                   |
| `DELETE` | `/books/{id}`                 | Delete book                   |
| `GET`    | `/search/book`                | Search books                  |
| `GET`    | `/books/{id}/ai-insights`     | Get AI-generated insights     |

8. **AI Integration**

   Uses Mistral's mistral-large-latest model

   Generates paragraph-length taglines from book metadata

   Handles API errors gracefully with 500 status codes



