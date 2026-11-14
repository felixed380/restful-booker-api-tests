# Restful-Booker API Test Automation Framework 🚧 *(Work in Progress)*

Automated API testing framework built with **Python**, **Pytest**, **Pydantic**, and **Faker**, integrated with **GitHub Actions** and **AI-assisted test design**.

## 🏗️ Project Architecture
- `src/client.py`: HTTP API client encapsulating endpoints and session management.
- `src/data_factory.py`: Dynamic test data generation using Faker.
- `src/schemas.py`: Response contract validation models with Pydantic *(in progress)*.
- `tests/`: Smoke, contract, CRUD, negative, and end-to-end workflow test suites.
- `ai_assisted/`: Prompt engineering logs and human code-review notes.

## 🚀 How to Run Locally
```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pytest -m smoke -v
```
