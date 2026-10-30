# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small task-list REST API with FastAPI to practice HTTP methods, JSON data, request validation, and status codes. You will create and test endpoints that let a client list, view, add, and delete tasks.

## 📝 Tasks

### 🛠️ Create the API and List Tasks

#### Description
Complete the starter code to create a FastAPI application and an endpoint for retrieving all tasks.

#### Requirements
Completed program should:

- Create a FastAPI application named `app`.
- Store tasks in the provided in-memory `tasks` list.
- Implement `GET /tasks` and return the current tasks as JSON.
- Start the development server with `uvicorn starter-code:app --reload` and confirm the endpoint works at `/docs`.

### 🛠️ Add and Retrieve Tasks

#### Description
Add endpoints for creating a task and retrieving one task by its ID. Use the provided Pydantic model to validate incoming task data.

#### Requirements
Completed program should:

- Implement `POST /tasks` to accept a JSON task with a title and optional `completed` value.
- Validate request data with the `TaskCreate` model and return the created task, including its assigned ID.
- Implement `GET /tasks/{task_id}` to return the matching task.
- Return an HTTP `404` response when the requested task ID does not exist.

For example, sending this JSON to `POST /tasks` should create a task:

```json
{
  "title": "Read FastAPI documentation",
  "completed": false
}
```

### 🛠️ Delete Tasks with REST Status Codes

#### Description
Implement an endpoint to delete a task by ID and use appropriate HTTP status codes to communicate success or errors.

#### Requirements
Completed program should:

- Implement `DELETE /tasks/{task_id}`.
- Remove and return no response body when a task is successfully deleted, using HTTP `204`.
- Return HTTP `404` when the task ID does not exist.
- Test the list, create, retrieve, and delete endpoints in FastAPI's interactive `/docs` page.
