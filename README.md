# django-employee-management-app
A simple Django Employee Management app powered by Django rest framework.

## How to Run the Project

1. Create your own virtual environment (Optional)
	
    python3 -m venv {FOLDER_NAME}

2. Run the Following Code to install the necessary dependencies
```
    pip install -r requirements.txt
```
3. Run the Following Code to initialize the project database.
```
    python manage.py makemigrations
    python manage.py migrate
   ```
4. Run the Following Code to run the server
```
    python manage.py runserver
```

5. Visit http://localhost:8000/ 
6. Login using the following credentials. Or You can register a user.
```	
    Username: "admin"
    Password: "password"
```
*Disclaimer: Some dummy data are preloaded in the sqlite.db file. All dummy data are generated in random using online tools.*
