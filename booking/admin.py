from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'number_of_people')  # Corrected 'number_of_pealpe' to 'number_of_people'

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'date', 'start_time', 'end_time', 'name', 'email')
