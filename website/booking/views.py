from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction



@login_required
def user_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'user_reservations.html', {'reservations': reservations})


@login_required
def make_reservation(request):
    if request.method == 'POST':
        user = request.user
        number_of_people = request.POST.get('number_of_people')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        name = request.POST.get('name')
        email = request.POST.get('email')

        
        available_tables = Table.objects.filter(number_of_people=number_of_people, is_available=True)
        if available_tables.exists():
            table = available_tables.first()

           
            reservation = Reservation.objects.create(user=user, table=table, number_of_people=number_of_people, date=date, start_time=start_time, end_time=end_time, name=name, email=email)

            reservation_url = f'/reservation/{reservation.id}/'
            return redirect(reservation_url)
        else:
            messages.error(request, 'No available table for the specified number of people.')
            return redirect('make_reservation')
    else:
        return render(request, 'make_reservation.html')

@login_required
def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, user=request.user)
    return render(request, 'reservation_detail.html', {'reservation': reservation})      


@login_required
def delete_reservation(request, reservation_id):
    try:
        with transaction.atomic():
           
            reservation = Reservation.objects.get(id=reservation_id, user=request.user)
            table = reservation.table
            reservation.delete()

            
            table.is_available = True
            table.save()

            messages.success(request, 'Reservation deleted successfully.')
    except Reservation.DoesNotExist:
        messages.error(request, 'Reservation does not exist or you are not authorized to delete it.')

    return redirect('home')