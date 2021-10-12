# CRM-API-AM

#Description
This is a project that implements a simple CRM system including an very simple user admin APIS; both components were built as API REST using DJango Framework and Django REST Framework; you can use this functions:

COSTUMERS
Costumer List: REST API that list the costumers (Method GET)
Costumer Details: REST API that shows de costumer details (Method GET)
Costumer Create: REST API to create a costumer (Method POST)
Costumer Update: REST API to update a costumer (Method UPDATE)
Costumer Delete: REST API to delete a costumer (Method DELETE)

USERS
User List: REST API that list the users (Method GET)
User Details: REST API that shows de user details (Method GET)
User Create: REST API to create a user (Method POST)
User Update: REST API to update a user (Method UPDATE)
User Delete: REST API to delete a user (Method DELETE)


ENDPOINTS
1. admin/ : In this Endpoint you can have access to the admin interface included with Django
2. login/ : Is a dummy access to get access to the app
3. api/costumer/: Endpoint to manage costumers
4. api/user/: Endpoint to manage users
5. logout/ : Dummy option to finish the user session

How to use the App
1. Clone the project
2. Install Python
3. Install Django
4. Install Django Rest Framework
5. Create a superuser to access de app: py manage.py createsuperuser
6. Execute initial migrations command one: py manage.py make migrations
7. Execute initial migrations command two: py manage.py make migrate
8. Run Server: py manage.py runserver
9. Open a webbrowser and use the URL that appears in the console after executed step 8.
10. Open enpoint "login" and use the superuser credentials
11. then you can navigate the REST enpoints using the FormView interface provided by Django REST Framework

Special Features
Access Control: there is an access control using tokens, you have to loggin if you want to manage users or costumers


