# ELD Trip Planner

This is a full-stack application built with Django and React to plan trips and generate ELD logs for truck drivers.

## Features

- Input trip details and calculate routes
- Generate daily log sheets
- Display routes on a map

## Technologies Used

- Backend: Django, Django REST Framework
- Frontend: React, Leaflet for maps
- Database: SQLite (for development)

## Setup Instructions

### Prerequisites

- Python 3.x
- Node.js and npm
- Git

### Backend Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aksh9106/backend.git
   cd backend/backend
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the backend server:**

   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the frontend server:**

   ```bash
   npm start
   ```

### Access the Application

- **API**: Visit `http://127.0.0.1:8000/api/trips/`
- **Admin Interface**: Visit `http://127.0.0.1:8000/admin/`
- **Frontend**: Visit `http://localhost:3000/`

## Deployment

- **Backend**: Deploy using Heroku or any other cloud service.
- **Frontend**: Deploy using Vercel or Netlify.

## License

This project is licensed under the MIT License.
