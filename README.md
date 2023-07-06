# Microblogging Platform

The Microblogging Platform is a Python Django-based microblogging web application that allows users to share short messages, follow other users, and interact with posts.

## Features

- User registration and authentication
- Creating and publishing posts
- Following and unfollowing other users
- Liking and commenting on posts
- Timeline view to see posts from followed users
- User profiles with bio and profile picture

## Installation

### Prerequisites

- Python 3.9 or higher
- PostgreSQL database
- Redis server

### Clone the Repository
```bash
git clone https://github.com/gnanee57/microblog.git
cd microblog
```

### Create and activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate
```
### Install the required packages
```bash
pip install -r requirements.txt
```

### Apply database migrations
```bash
python manage.py migrate
```

### Update the `settings.py` file
- Set the `SECRET_KEY` to a secure value.
- Configure the database settings in the `DATABASES` dictionary.
- Set the `REDIS_URL` to the Redis server URL.

### Start the development server
```bash
python manage.py runserver
```


The Microblogging Platform will now be accessible at `http://localhost:8000/`.

## API Endpoints

- **Create User**
- Endpoint: `/api/users/`
- Method: POST

- **Retrieve User**
- Endpoint: `/api/users/<int:user_id>/`
- Method: GET

- **Update User**
- Endpoint: `/api/users/<int:user_id>/`
- Method: PUT/PATCH

- **Create Post**
- Endpoint: `/api/posts/`
- Method: POST

- **Retrieve Post**
- Endpoint: `/api/posts/<int:post_id>/`
- Method: GET

- **Update Post**
- Endpoint: `/api/posts/<int:post_id>/`
- Method: PUT/PATCH

- **Delete Post**
- Endpoint: `/api/posts/<int:post_id>/`
- Method: DELETE

- **List Posts**
- Endpoint: `/api/posts/`
- Method: GET

## Caching

The user timeline endpoint is cached using Redis to improve performance.

## Error Handling

The API follows RESTful principles for error handling. Error responses include the appropriate HTTP status code and an error message in the response body.

## License

This project is licensed under the [MIT License](LICENSE).

