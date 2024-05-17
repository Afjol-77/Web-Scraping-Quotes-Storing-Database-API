# Web Scraping Quotes, Storing to Database and getting response with API
A web scraping script which is scraping quotes from BrainyQuote and storing the quotes in a database. The data is accessible through a Django Rest Framework API.

**Used Technologies:** 
* Django REST Framework

**Database**
* SQLite 3

## How to run this app on your machine? <br>
### 1. Extract and open the project, then install the api_script_req.txt for API Script in a virtual environment
```
pip install -r api_script_req.txt
```
### 2. Similarly install the scrap_script_req.txt for Web Scraping Script in a virtual environment
```
pip install -r scrap_script_req.txt
```

### 3. For migrations, type this on your terminal in API Script directory and create a superuser
```
python manage.py makemigrations
python manage.py migrate
```

```
python manage.py createsuperuser
```

### 4. Insert your database path in Web Scraping Script and Run the script
```
connection = sqlite3.connect('Please Insert Your Database Path')
```
### 5. Run the DRF project server using the following command
```
python manage.py runserver
```


Your Django project is **LIVE** now on your localhost. <br>
Open your browser and type **127.0.0.1:8000** on address bar.<br>
<br>

To access data through API, visit **http://127.0.0.1:8000/api/**

Similarly, create, delete, retrieve operations can be done by heading to the URLs mentioned in the urls.py file


This is an screenshot of API view:


![screenshot](https://github.com/Afjol-77/Web-Scraping-Quotes-Storing-Database-API/blob/main/ss.png?raw=true)
___
### THANK YOU!
