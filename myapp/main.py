from typing import List
import datetime

from fastapi import FastAPI
from django.core import serializers
from myapp.models import Article, Reporter
from myapp.pydantic_models import ArticleModel, ReporterModel

# Initialize FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Django ORM"}


@app.get("/articles/", response_model=List[ArticleModel])
def get_article():
    items = Article.objects.select_related('reporter').all()
    articles = []

    for item in items:
        # Convert pub_date to string if it's a date object
        pub_date_str = item.pub_date.isoformat() if isinstance(item.pub_date, (datetime.date, datetime.datetime)) else item.pub_date

        # Convert reporter instance to ReporterModel
        reporter_instance = item.reporter
        reporter = ReporterModel.model_validate(reporter_instance)

        # Create ArticleModel instance
        article = ArticleModel(
            headline=item.headline,
            pub_date=pub_date_str,
            reporter=reporter
        )
        articles.append(article)

    return articles


@app.get("/reporters/", response_model=ReporterModel)
def create_reporter(first_name: str, last_name: str, email: str):
    item = Reporter.objects.create(first_name=first_name, last_name=last_name, email=email)
    return {"id": item.id, "name": item.name, "age": item.age}


@app.post("/articles/", response_model=ArticleModel)
def create_article(headline: str, reporter: int):
    item = Article.objects.create(headline=headline, reporter=reporter)
    return {"id": item.id, "name": item.name, "age": item.age}
