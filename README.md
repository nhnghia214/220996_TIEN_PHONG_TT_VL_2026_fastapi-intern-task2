# FastAPI Internship Task 2

Backend API project built with **FastAPI** following a modular architecture.

## Features

- JWT Authentication
- File Upload API
- OpenAI Chatbot API
- Environment configuration using `.env`
- Clean modular project structure

---

# Project Structure


api_base
│
├── app
│ ├── routers
│ │ ├── auth.py
│ │ ├── base.py
│ │ ├── file_upload.py
│ │ └── chatbot.py
│ │
│ ├── security
│ │ └── security.py
│ │
│ └── config.py
│
├── chatbot
│ └── services
│ └── chatbot_service.py
│
├── utils
│ └── upload_temp
│
├── run_api.py
├── requirements.txt
└── README.md


---

# Installation

## 1. Clone repository


git clone https://github.com/nhnghia214/220996_TIEN_PHONG_TT_VL_2026_fastapi-intern-task2.git


---

## 2. Create virtual environment


python -m venv venv


---

## 3. Activate environment

Windows:


venv\Scripts\activate


---

## 4. Install dependencies


pip install -r requirements.txt


---

## 5. Configure environment variables

Create file `.env`


OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxx # nằm ở file .env
SECRET_KEY=xxxxxxxxxx # nằm ở file .env


---

## 6. Run server


python run_api.py


---

## 7. API Documentation (Swagger)

Open in browser:


http://localhost:8000/docs


Available APIs:

- `GET /`
- `GET /health`
- `POST /auth/login`
- `POST /file/upload`
- `POST /chatbot/ask`

---

# Technologies Used

- FastAPI
- Uvicorn
- JWT (python-jose)
- Passlib (password hashing)
- OpenAI API
- Python-dotenv