from django.db import models


class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    number_of_people = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - Number of People: {self.number_of_people}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set default user
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    number_of_people = models.IntegerField(default=1) 
    date = models.DateField()
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Reservation for {self.table} - {self.date} from {self.start_time} to {self.end_time}"