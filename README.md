FASTAPI INTERNSHIP – TASK 2
Backend API Project

Student: Hoàng Nghĩa
Project: FastAPI Backend Internship Task 2

--------------------------------------------------

GitHub Repository:

https://github.com/nhnghia214/220996_TIEN_PHONG_TT_VL_2026_fastapi-intern-task2

--------------------------------------------------

Project Description

This project is a backend API built using FastAPI following a modular architecture.
It demonstrates common backend functionalities including authentication,
file upload, and AI chatbot integration.

--------------------------------------------------

Main Features

1. JWT Authentication
   - Login API using JWT token

2. File Upload API
   - Upload files to server

3. OpenAI Chatbot API
   - Ask questions and receive AI responses

4. Environment Configuration
   - Uses .env file to manage sensitive information

5. Modular Project Structure
   - Organized routers, services, and utilities

--------------------------------------------------

API Endpoints

GET  /                 -> Check API running
GET  /health           -> Health check

POST /auth/login       -> User login (JWT authentication)
POST /file/upload      -> Upload file to server
POST /chatbot/ask      -> Ask AI chatbot

--------------------------------------------------

How to Run the Project

1. Clone the repository

git clone https://github.com/nhnghia214/220996_TIEN_PHONG_TT_VL_2026_fastapi-intern-task2


2. Move to project folder

cd 220996_TIEN_PHONG_TT_VL_2026_fastapi-intern-task2


3. Create virtual environment

python -m venv venv


4. Activate environment

Windows:

venv\Scripts\activate


5. Install required libraries

pip install -r requirements.txt


6. Create environment configuration file

Create a file named:

.env

Add the following variables:


OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx # nằm ở file .env
SECRET_KEY=xxxxxxxxxx # nằm ở file .env


7. Run the FastAPI server

python run_api.py


8. Open API documentation (Swagger)

http://localhost:8000/docs

--------------------------------------------------

Technologies Used

FastAPI
Uvicorn
JWT (python-jose)
Passlib
OpenAI API
Python-dotenv

--------------------------------------------------

End of document