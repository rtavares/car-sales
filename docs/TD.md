# Car selling platform project

## Technical description

### This documents describes the development roadmap
- Project will be developed using Python, Django and Django Rest Framework
- Project should follow TDD using Pytest
- Git development branches should follow this TD numeration

Note: Test are not referred in tasks, once we should do TDD


1 - Basic installation
1.1 - Create Virtual environment using `uv`    
1.2 - Install Django,  Django Rest Framework, Pytest.
- corsheaders could be necessary for local testing
1.2.1 - Complementary tools: ruff for code format, imports sort and linting.   
2 - Create base Django project and add external modules   
2.1 - Create a base app   
3 - Create a User Profile app   
- Extending User, in order to add extra fields for additional information, like location   
4  - Create Cars App   
4.1 - Create models     
4.2 - Enable models in Admin   
4.3 - Create serializers   
4.4 - create views   
4.5 - Create endpoints / urls for CRUD operations
5 - Create authentication / authorization
6 - Create Messages App 
    - Note: we could choose to use an existing application, like django-postman
6.1 - Create models     
    - From, To, Subject, Body, Delivery date, read, read date.
6.2 - Enable model in Admin   
6.3 - Create serializers   
6.4 - create views   
6.5 - Create endpoints / urls for CRUD operations

-------------


