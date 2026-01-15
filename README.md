# Employee Management System – Backend API

## Project Overview
The Employee Management System is a backend‑only RESTful API developed using Python and FastAPI.  
The project focuses on secure authentication, efficient employee data management and cloud deployment.  
No frontend is included, making this a pure backend system that can integrate with any client application.

---

## Key Features
- Backend‑only REST API
- JWT‑based authentication
- Secure password hashing
- Employee data management (CRUD)
- Input validation and error handling
- Automated testing using Pytest
- Cloud‑deployed and platform‑independent

---

## Technology Stack
- Language: Python  
- Framework: FastAPI  
- Authentication: JWT (JSON Web Token)  
- Database: SQLite  
- ORM: SQLAlchemy  
- Testing: Pytest  
- Deployment: Render  

---

## System Architecture
The project follows a Client–Server REST architecture:

Client (Postman / Any App)  
→ FastAPI Backend  
→ Database (SQLite)

All requests and responses are exchanged in JSON format.

---

## API Functionality
### Authentication
- User login
- JWT token generation
- Token‑based access control for protected routes

### Employee Management
- Create new employee
- Fetch all employees
- Fetch employee by ID
- Prevent duplicate email entries
- Handle invalid requests gracefully

---

## Security
- Passwords are hashed using bcrypt
- JWT tokens secure all protected endpoints
- Unauthorized access is blocked

---

## Testing
Automated tests are implemented using Pytest to verify:
- Employee creation
- Duplicate email handling
- Fetching employee data
- Invalid request handling

---

## Deployment
The backend is deployed on Render, providing:
- A live API URL
- No local setup requirement
- Access from any system or device

---

## Conclusion
This project demonstrates strong backend development skills, including secure API design, clean architecture and real‑world cloud deployment. It is suitable for backend developer interviews, academic submissions and API‑based applications.
