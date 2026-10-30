import sqlite3
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Persistent Task List API")
DATABASE_PATH = Path(__file__).with_name("tasks.db")


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    completed: bool


def get_connection() -> sqlite3.Connection:
    """Open a connection to the assignment's SQLite database."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    """Create the tasks table if it does not already exist."""
    # TODO: Connect to the database and create a tasks table with:
    # id (INTEGER PRIMARY KEY), title (TEXT NOT NULL),
    # completed (INTEGER NOT NULL DEFAULT 0).
    pass


def row_to_task(row: sqlite3.Row) -> dict[str, Any]:
    """Convert a database row into the JSON shape returned by the API."""
    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
    }


@app.on_event("startup")
def startup() -> None:
    initialize_database()


@app.get("/tasks")
def list_tasks() -> list[dict[str, Any]]:
    # TODO: Query all tasks and return them using row_to_task.
    return []


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate) -> dict[str, Any]:
    # TODO: Insert the task using a parameterized query, then return the
    # saved task including its generated ID.
    raise NotImplementedError


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> dict[str, Any]:
    # TODO: Fetch by ID. If no row is found, raise HTTPException(404).
    raise NotImplementedError


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate) -> dict[str, Any]:
    # TODO: Update completed using a parameterized query and return the task.
    # Raise HTTPException(404) if the task does not exist.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Delete using a parameterized query. If no row was deleted,
    # raise HTTPException(404). Otherwise return an empty 204 Response.
    raise NotImplementedError
