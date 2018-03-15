from django.db import models
from mongoengine import *
from autotest.settings import DBNAME, _MONGODB_DATABASE_HOST

connect(DBNAME)

# Create your models here.


class UserStory(Document):
    # US_ID = StringField(max_length=120, required=True)

    US_ID = StringField(max_length=120, required=True)

    US_Name = StringField(max_length=120, required=True)
    US_As = StringField(max_length=120, required=True)
    US_IWant = StringField(max_length=120, required=True)
    US_SoThat = StringField(max_length=120, required=True)
    US_Priority = StringField(max_length=120, required=True)

    # AC_Name = StringField(max_length=120, required=True)
    # AC_Given = StringField(max_length=120, required=True)
    # AC_When = StringField(max_length=120, required=True)
    # AC_Then = StringField(max_length=120, required=True)
    # AC_Negative = BooleanField(required=True)


# class AcceptanceCriteria(Document):
#     AC_Name = StringField(max_length=120, required=True)
#     AC_Given = StringField(max_length=120, required=True)
#     AC_When = StringField(max_length=120, required=True)
#     AC_Then = StringField(max_length=120, required=True)
#     AC_Negative = BooleanField(required=True)