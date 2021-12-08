from django.forms import (
    Form,
    CharField,
)


class StudentForm(Form):
    name = CharField()
    grades = CharField()
