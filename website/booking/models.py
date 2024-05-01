from django.db import models


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    number_of_people = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - Number of People: {self.number_of_people}"