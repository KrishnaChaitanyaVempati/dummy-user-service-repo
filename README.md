# Dummy User Service

This is a small FastAPI microservice repo created to validate the Git ingestion pipeline.

## What it exposes

- `GET /health` for service health
- `GET /users/{user_id}` to fetch a single user
- `POST /users` to create a user

## Repo layout

- `openapi/openapi.yaml`: OpenAPI definition for endpoint-aware ingestion
- `app/main.py`: FastAPI application entrypoint
- `app/routers/users.py`: Route handlers with tags, summaries, and docstrings
- `app/schemas/users.py`: Request and response models

## Why this repo exists

The agentic Git pipeline can ingest this repo in two ways:

1. From the OpenAPI file as structured API operations
2. From the FastAPI route decorators as endpoint-aware code documents

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
