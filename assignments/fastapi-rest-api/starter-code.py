from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task List API")

# Temporary in-memory storage; tasks reset whenever the server restarts.
tasks = []


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


# TODO: Add GET /tasks to return all tasks.

# TODO: Add POST /tasks. Accept TaskCreate, assign a unique integer ID,
# store the task, and return the created task.

# TODO: Add GET /tasks/{task_id}. Return the matching task or raise
# HTTPException with status code 404 if it does not exist.

# TODO: Add DELETE /tasks/{task_id}. Remove the matching task and return
# an empty 204 response, or raise HTTPException with status code 404.
