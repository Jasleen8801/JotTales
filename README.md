# JotTales

This is a simple blog application developed using Django, Django REST framework, and React Native.

## Project Overview

The project consists of two main parts: the backend, built with Django and Django REST framework, and the frontend, built with React Native. The backend serves as the API for the blog application, while the frontend provides a mobile app to interact with the API.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- View blog post details, including author information
- Upload and display images for blog posts
- User profile with an option to update profile picture
- Admin panel to manage blog posts and users

## Tech Stack

- Django: Backend web framework
- Django REST framework: API development
- React Native: Frontend mobile app development
- SQLite: Database

## Installation and Setup

### Backend (Django)

1. Clone the repository:

```bash
git clone https://github.com/Jasleen8801/JotTales.git
cd JotTales/backend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Perform database migartions:

```bash
python manage.py migrate
```

5. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

The backend API will be available at `http://localhost:8000/`.

### Frontend (React Native)

`Note`: To be done

## Usage

Once the development server and the React Native app are running, you can use the mobile app to register, log in, create blog posts, view posts, and update your profile. Additionally, you can access the Django admin panel at `http://localhost:8000/admin/` to manage blog posts and users.