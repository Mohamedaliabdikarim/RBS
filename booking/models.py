from django.db import models, migrations
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    number_of_people = models.IntegerField(validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - Number of People: {self.number_of_people}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    number_of_people = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField()
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"Reservation for {self.table} - {self.date} from {self.start_time} to {self.end_time}"


def add_default_user(apps, schema_editor):
    Reservation = apps.get_model('booking', 'Reservation')
    User = apps.get_model('auth', 'User')
    default_user = User.objects.first() 
    Reservation.objects.filter(user__isnull=True).update(user=user)

class Migration(migrations.Migration):
    dependencies = [
        ('booking', 'previous_migration'),  
    ]
    operations = [
        migrations.RunPython(add_default_user),
        
    ]