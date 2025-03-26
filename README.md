# Task Management API

A RESTful API for task management built with Django and Django Rest Framework. This API allows users to create tasks, assign tasks to users, and retrieve tasks assigned to specific users.

## Features

- Create tasks with name, description, and task type
- Assign tasks to one or multiple users
- Retrieve all tasks assigned to a specific user
- User management

## Technology Stack

- Python 3.x
- Django 5.1.7
- Django Rest Framework 3.15.2
- SQLite (default database)

## Project Structure

The project consists of two main apps:

1. **users**: Handles user-related functionality
2. **tasks**: Handles task-related functionality

## Models

### User Model

Extends Django's AbstractUser and adds:
- Mobile number

### Task Model

Represents a task with the following fields:
- Name
- Description
- Created at timestamp
- Task type (Personal, Work, Study)
- Completed at timestamp
- Status (Pending, In Progress, Completed)
- Assigned users (Many-to-Many relationship with User)

## API Endpoints

### User Endpoints

- `GET /api/users/`: List all users

### Task Endpoints

- `POST /api/tasks/create/`: Create a new task
- `POST /api/tasks/<task_id>/assign/`: Assign a task to one or multiple users
- `GET /api/tasks/user/<user_id>/`: Get all tasks assigned to a specific user

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/himanshuxcode/task_management_backend.git
   cd task_management
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the API at `http://127.0.0.1:8000/api/`

## API Usage Examples

### Create a Task

**Request:**
```http
POST /api/tasks/create/
Content-Type: application/json

{
    "name": "Complete Project Documentation",
    "description": "Write comprehensive documentation for the task management API",
    "task_type": "W"
}
```

**Response:**
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Complete Project Documentation",
        "description": "Write comprehensive documentation for the task management API",
        "created_at": "2025-03-26T08:30:00Z",
        "task_type": "W",
        "completed_at": null,
        "status": "P",
        "assigned_users": []
    },
    "message": "Task created successfully"
}
```

### Assign a Task to Users

**Request:**
```http
POST /api/tasks/1/assign/
Content-Type: application/json

{
    "user_ids": [1, 2]
}
```

**Response:**
```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "Complete Project Documentation",
        "description": "Write comprehensive documentation for the task management API",
        "created_at": "2025-03-26T08:30:00Z",
        "task_type": "W",
        "completed_at": null,
        "status": "P",
        "assigned_users": [
            {
                "id": 1,
                "username": "admin",
                "email": "admin@example.com",
                "mobile": null,
                "first_name": "Admin",
                "last_name": "User"
            },
            {
                "id": 2,
                "username": "user1",
                "email": "user1@example.com",
                "mobile": "1234567890",
                "first_name": "Test",
                "last_name": "User"
            }
        ]
    },
    "message": "Task assigned successfully"
}
```

### Get Tasks for a Specific User

**Request:**
```http
GET /api/tasks/user/1/
```

**Response:**
```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "Complete Project Documentation",
            "description": "Write comprehensive documentation for the task management API",
            "created_at": "2025-03-26T08:30:00Z",
            "task_type": "W",
            "completed_at": null,
            "status": "P",
            "assigned_users": [
                {
                    "id": 1,
                    "username": "admin",
                    "email": "admin@example.com",
                    "mobile": null,
                    "first_name": "Admin",
                    "last_name": "User"
                },
                {
                    "id": 2,
                    "username": "user1",
                    "email": "user1@example.com",
                    "mobile": "1234567890",
                    "first_name": "Test",
                    "last_name": "User"
                }
            ]
        }
    ],
    "message": ""
}
```

## Task Types

- `P`: Personal
- `W`: Work
- `S`: Study

## Task Status

- `P`: Pending
- `IP`: In Progress
- `C`: Completed

## Test Credentials

After setting up the project and creating a superuser, you can use the following credentials for testing:

- **Admin User**:
  - Username: admin
  - Password: (the password you set during `createsuperuser` command)

## Admin Interface

Django's admin interface is available at `http://127.0.0.1:8000/admin/` where you can manage users and tasks.

## Error Handling

The API returns standardized error responses with appropriate HTTP status codes and error messages.
