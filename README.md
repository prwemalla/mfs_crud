The Problem:
============
###Sample application consisting of:
1. A frontend in vue
2. An authentication service in Python 3
3. A task management service in python 3
The 3 services communicate to each other via an API.

###The application supports the folliwing functions:
1. Login / Logout Access Control with User authentication using JWT tokens
2. An interface to manage tasks allowing you to Create, Update, Delete, List and View Tasks
3. An admin interface that Enables Admins to Add, Update, List, View and Delete users.

###Constraints:
1. Number of services is 3:
2. Support Authentication
3. 2 backend services in python

Interpretation of the problem:
I need to develop an application with striclty 3 services but supports authentication that means one of the services has to be an authentication service.
The next service has to be the front end. Leaving me to chose the last service so i went with a simple task management service. Since i can create another service,
i can not have a dedicated database server so i shall just use sqlite database.

###Proposed Solution:
Services:
    1. Front End service:
        * Technology: Vue JS application
        * Communication: API
        * Security: JWT tokens
        * Login / Logout
        * User Views:
            * Create User
            * List Users
            * Update User
            * View User
            * Delete User
        * Ticket CRUDL
            * Create Task
            * List Tasks
            * Update Task
            * View Task
            * Delete Task
    2. Authentication Service:
        * Technology: Python 3
        * Communication API
        * Security: JWT tokens
        * Service API's:
            * POST: http://localhost:8080/auth/api/v1/user/
            * DELETE: http://localhost:8080/auth/api/v1/user/{id}/
            * GET: http://localhost:8080/auth/api/v1/user/
            * GET: http://localhost:8080/auth/api/v1/user/{id}/
            * PUT: http://localhost:8080/auth/api/v1/user/{id}/
        * Authentication API's:
            * POST: http://localhost:8080/auth/login
            * POST: http://localhost:8080/auth/refresh
            * GET: http://localhost:8080/auth/user
            * POST: http://localhost:8080/auth/verify
    2. Task Service:
        * Technology: Python 3
        * Communication API
        * Security: JWT tokens
        * API's:
            * POST: http://127.0.0.1:8000/task_service/api/v1/task/
            * DELETE: http://127.0.0.1:8000/task_service/api/v1/task/{id}/
            * GET: http://127.0.0.1:8000/task_service/api/v1/task/
            * GET: http://127.0.0.1:8000/task_service/api/v1/task/{id}/
            * PUT: http://127.0.0.1:8000/task_service/api/v1/task/{id}/

How to run:
1. Clone repo
2. open terminal in project directory
3. run command:
```sh
docker-compose up --build to start the project
 ```
4. to run the application Browse to: 
```sh
http://localhost:8888/
 ```
