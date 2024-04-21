# DataRoot University: Data Science Fundamentals. Flask project

The project plan is as follows:

1. Create database and connect to it
2. Create Models of Actors and Movies
3. Create methods for interaction with Models (commit(), create(), update() etc.)
4. Create methods for correct processing requests and handling errors (controllers) (get_actor_by_id(), add_movie()
   etc.)
5. Create routes for app corresponding to our controllers
6. Test your app
7. Dockerize your app

## Folder structure

In this project, Model-View-Controller (MVC) pattern is used. The project structure is as follows:

```
app
    ├──  models                 - this folder contains all database models.
    │   ├── __init__.py         - init file for the package.
    │   ├── base.py             - this file contains class Model which handles all data-management operations. Actor and Movie classes will be inherited from it.
    │   ├── actor.py            - Actor entity model.
    │   ├── movie.py            - Movie entity model.
    |   └── relations.py        - association table for Actor and Movie entities. 
    │
    │
    ├── controllers             - this folder contains all commands operations handlers.
    │   ├── actor.py            - handlers for operations related to the Actor entity.
    │   ├── movie.py            - handlers for operations related to the Movie entity.
    │   └── parse_request.py    - this file contains a function which parses request data and converts it to a convenient format.
    │   
    │   
    ├── settings                - here you can store different constant values, connection parameters, etc.
    │   └── constants.py        -  multiple constants storage for their convenient usage.
    │ 
    │ 
    ├── core                    - folder, which contains core application components.
    │   ├── __init__.py         - initializing our app and DB.
    │   └── routes.py           - application routes (predefined commands).
    │
    ├── tests                   - this folder contains test cases for testing the correctness of operation handlers.
    │   ├── actor_test.py       - test cases of basic handlers for operations related to the Actor entity.
    │   ├── movie_test.py       - test cases of basic handlers for operations related to the Movie entity.
    │   └── relationships_test.py - test cases of relationship handlers between Movie and Actor entities.
    │   
    ├── run.py                  - application run file.
    |
    ├── Dockerfile				- commands used for Dockerization
    |
    └── requirements.txt		- list of libraries used for Dockerization
```