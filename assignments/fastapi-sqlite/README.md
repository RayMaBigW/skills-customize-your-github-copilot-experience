# 📘 Assignment: Persist FastAPI Data with SQLite

## 🎯 Objective

Extend a FastAPI task-list API to save and retrieve tasks using SQLite. Practice basic database operations and connect persistent storage to API endpoints.

## 📝 Tasks

### 🛠️ Create a SQLite Database

#### Description
Set up a SQLite database and a `tasks` table for the task-list API. Use the provided starter code and create the database and table when the application starts.

#### Requirements
Completed program should:

- Create or open a local SQLite database file named `tasks.db`.
- Create a `tasks` table with an integer primary key, a required title, and a completed flag.
- Initialize the database table automatically when the application starts.
- Keep database connection and query logic in small, reusable functions.

### 🛠️ Persist and Retrieve Tasks Through the API

#### Description
Update the API endpoints to use SQLite instead of an in-memory list, so task data remains available after the server restarts.

#### Requirements
Completed program should:

- Make `GET /tasks` return all tasks stored in the database as JSON.
- Make `POST /tasks` validate the request with the provided Pydantic model, insert the task, and return the saved task and its generated ID.
- Make `GET /tasks/{task_id}` return the stored task or an HTTP `404` response when it does not exist.
- Use parameterized SQL queries for database values.

### 🛠️ Update and Delete Stored Tasks

#### Description
Add database-backed endpoints to mark a task complete and delete a task. Verify that updates and deletions change the persisted data.

#### Requirements
Completed program should:

- Implement `PATCH /tasks/{task_id}` to update the task's completed state.
- Implement `DELETE /tasks/{task_id}` and return HTTP `204` when a task is deleted.
- Return HTTP `404` if an update or deletion targets a task ID that does not exist.
- Restart the server and confirm that created tasks remain stored in SQLite.
