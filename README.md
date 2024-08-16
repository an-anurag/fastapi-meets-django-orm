## FastAPI meets Django ORM

This is a simple project to show how to use FastAPI with Django ORM.



### Installation
```bash
pip install -r requirements.txt
```

### Migrate
```bash
python manage.py makemigrations
python manage.py migrate
```

### Add some data
```bash
python manage.py shell
>>> r = Reporter(first_name="John", last_name="Smith", email="john@example.com")
>>> r.save()

>>> r2 = Reporter(first_name="Paul", last_name="Jones", email="paul@example.com")
>>> r2.save()

>>> a = Article(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
>>> a.save()

>>> Article.objects.create(headline="Paul's story", pub_date=date(2006, 1, 17), reporter=r)
```


### Run
```bash
uvicorn myapp.main:app --reload
```