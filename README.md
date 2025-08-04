
# 🚀 FastAPI Learning Playground

An end-to-end journey through building modern, production-ready APIs using **FastAPI** — covering routing, request validation, model inference, file uploads, background tasks, and Docker deployment.

✅ **10 hands-on examples** with modular scripts — beginner to advanced.

---

## 📂 Project Structure

```bash
fastapi-project/
├── app/
│   ├── 01_path_query_params.py       # Path and query parameters
│   ├── 02_body_validation.py         # Pydantic request body validation
│   ├── 03_model_serving.py           # ML-style prediction API
│   ├── 04_error_handling.py          # Custom error responses
│   ├── 05_response_models.py         # Response model shaping
│   ├── 06_dependency_injection.py    # Shared logic with Depends()
│   ├── 07_cors_and_headers.py        # CORS and custom headers
│   ├── 08_file_upload.py             # File upload via form/Swagger
│   ├── 09_background_tasks.py        # Background processing
│   ├── 10_docker_deployment.py       # (Placeholder for Docker lesson)
├── Dockerfile                        # Docker setup for deployment
├── requirements.txt                  # Python dependencies
├── README.md                         # The file you're reading!
````

---

## 🧰 Tech Stack

* ✅ Python 3.10+
* ⚡ FastAPI
* 🧪 Pydantic
* 🔧 Uvicorn
* 🐳 Docker (for deployment)
* 🌍 OpenAPI Docs (auto-generated)
* 🧠 *Optional:* ML logic simulation

---

## ▶️ Getting Started

### Clone the repo

```bash
git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project
```

### Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run any example

```bash
uvicorn app.03_model_serving:app --reload
```

Replace `03_model_serving` with any script (01–10) to explore that specific lesson.

---

## 🐳 Docker Setup (Optional)

### Build the Docker image

```bash
docker build -t fastapi-app .
```

### Run the Docker container

```bash
docker run -p 8000:8000 fastapi-app
```

Then visit in your browser:

* [http://localhost:8000/docs](http://localhost:8000/docs) → Swagger UI
* [http://localhost:8000/redoc](http://localhost:8000/redoc) → ReDoc

---

## ✅ What You’ll Learn

| Lesson | Topics                              |
| ------ | ----------------------------------- |
| 01     | Path + Query Parameters             |
| 02     | POST Requests + Pydantic Validation |
| 03     | ML Model Serving (simulated)        |
| 04     | Error Handling (404, 400, etc.)     |
| 05     | Response Models (filter fields)     |
| 06     | Dependency Injection (Depends)      |
| 07     | CORS + Custom Response Headers      |
| 08     | File Upload (CSV/Image/Etc.)        |
| 09     | Background Tasks (logging, async)   |
| 10     | Docker Deployment                   |

---

## 📌 License

This project is **open-source** and free to use for educational and portfolio purposes.

---

## 🙌 Acknowledgments

Big thanks to [@tiangolo](https://github.com/tiangolo) for creating **FastAPI**!


