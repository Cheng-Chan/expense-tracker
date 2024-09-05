# Expense Tracker Application

## Project Description

An example of CRUD APIs built with FastAPI, integrated with a PostgreSQL database.

## Table of Contents

- [Project Description](#project-description)
- [Setup](#setup)
  - [Database Setup with Docker Compose](#database-setup-with-docker-compose)
  - [Environment Variables](#environment-variables)
  - [Create and Activate Virtual Environment](#create-and-activate-virtual-environment)
  - [Install Requirements](#install-requirements)
  - [Run the Project](#run-the-project)

## Setup

### Database Setup with Docker Compose

To set up the PostgreSQL database using Docker Compose, use the following configuration:

```yaml
version: "3.9"

services:
  postgres:
    image: postgres:14
    ports:
      - 5400:5432
    volumes:
      - ~/home/zayn/Documents/volume:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=zayn
      - POSTGRES_USER=postgres
      - POSTGRES_DB=expense_tracker
```

To run the database service, execute:

```console
docker compose -f compose-db.yml up -d
```

Create schema in your database

```console
CREATE SCHEMA expense;
```

Set up the following environment variables in a .env.local file:

```console
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=zayn
DATABASE_HOST=localhost
DATABASE_PORT=5400
DATABASE_NAME=expense_tracker
```

Create a virtual environment for the project:

```console
python3 -m venv venv
```

Activate the virtual environment:

```console
pip install -r requirements.txt
```

Start the FastAPI server using Uvicorn:

```console
uvicorn main:app --reload
```

The project will be accessible at http://localhost:8000.

This `README.md` includes the full setup instructions and details to get your FastAPI Expense Tracker application up and running. If you need more information or additional sections, feel free to ask!

```

```
