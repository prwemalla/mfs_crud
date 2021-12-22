The Problem:
============
### Sample application consisting of:
1. A frontend in vue
2. An authentication service in Python 3
3. A task management service in python 3
The 3 services communicate to each other via an API.

### The application supports the folliwing functions:
1. Login / Logout Access Control with User authentication using JWT tokens
2. An interface to manage tasks allowing you to Create, Update, Delete, List and View Tasks
3. An admin interface that Enables Admins to Add, Update, List, View and Delete users.

### Constraints:
1. Number of services is 3:
2. Support Authentication
3. 2 backend services in python

Interpretation of the problem:
I need to develop an application with striclty 3 services but supports authentication that means one of the services has to be an authentication service.
The next service has to be the front end. Leaving me to chose the last service so i went with a simple task management service. Since i can create another service,
i can not have a dedicated database server so i shall just use sqlite database.

### Proposed Solution:
Services:
<ol>
    <li>1. Front End service:</li>
    <ol>
        <li>* Technology: Vue JS application</li>
        <li>* Communication: API</li>
        <li>* Security: JWT tokens</li>
        <li>* Login / Logout</li>
        <li>* User Views:</li>
        <ol>
            <li>* Create User</li>
            <li>* List Users</li>
            <li>* Update User</li>
            <li>* View User</li>
            <li>* Delete User</li>
        </ol>
        <li>* Ticket CRUDL</li>
        <ol>
            <li>* Create Task</li>
            <li>* List Tasks</li>
            <li>* Update Task</li>
            <li>* View Task</li>
            <li>* Delete Task</li>
        </ol>
    </ol>
    <li>2. Authentication Service:</li>
    <ol>
        <li>* Technology: Python 3</li>
        <li>* Communication API</li>
        <li>* Security: JWT tokens</li>
        <li>* Service API's:</li>
        <ol>
            <li>* POST: http://localhost:8080/auth/api/v1/user/</li>
            <li>* DELETE: http://localhost:8080/auth/api/v1/user/{id}/</li>
            <li>* GET: http://localhost:8080/auth/api/v1/user/</li>
            <li>* GET: http://localhost:8080/auth/api/v1/user/{id}/</li>
            <li>* PUT: http://localhost:8080/auth/api/v1/user/{id}/</li>
        </ol>
        <li>* Authentication API's:</li>
        <ol>
            <li>* POST: http://localhost:8080/auth/login</li>
            <li>* POST: http://localhost:8080/auth/refresh</li>
            <li>* GET: http://localhost:8080/auth/user</li>
            <li>* POST: http://localhost:8080/auth/verify</li>
        </ol>
    </ol>
    <li>2. Task Service:</li>
    <ol>
        <li>* Technology: Python 3</li>
        <li>* Communication API</li>
        <li>* Security: JWT tokens</li>
        <li>* API's:</li>
        <ol>
            <li>* POST: http://127.0.0.1:8000/task_service/api/v1/task/</li>
            <li>* DELETE: http://127.0.0.1:8000/task_service/api/v1/task/{id}/</li>
            <li>* GET: http://127.0.0.1:8000/task_service/api/v1/task/</li>
            <li>* GET: http://127.0.0.1:8000/task_service/api/v1/task/{id}/</li>
            <li>* PUT: http://127.0.0.1:8000/task_service/api/v1/task/{id}/</li>
        </ol>
    </ol>
</ol>

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
