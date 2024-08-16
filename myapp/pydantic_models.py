# pydantic_models.py
from pydantic import BaseModel
from typing import Optional


class ReporterModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: Optional[str]

    class Config:
        from_attributes = True


class ArticleModel(BaseModel):
    headline: str
    pub_date: str
    reporter: ReporterModel  # Nested Pydantic model

    class Config:
        from_attributes = True
