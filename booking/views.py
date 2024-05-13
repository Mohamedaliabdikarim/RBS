from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import ReservationForm
from django.utils import timezone
from django.utils.translation import gettext_lazy as _




@login_required
def user_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'user_reservations.html', {'reservations': reservations})


@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            user = request.user
            number_of_people = form.cleaned_data['number_of_people']
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            if date < timezone.now().date():
                messages.error(request, 'Reservation date cannot be in the past.')
                return redirect('make_reservation')

            if end_time <= start_time:
                messages.error(request, 'End time must be after start time.')
                return redirect('make_reservation')

            existing_reservation = Reservation.objects.filter(table__number_of_people=number_of_people,
                                                              table__is_available=True,
                                                              date=date,
                                                              start_time__lt=end_time,
                                                              end_time__gt=start_time)
            if existing_reservation.exists():
                messages.error(request, 'The selected table is already booked for the specified time.')
                return redirect('make_reservation')
            else:
                with transaction.atomic():
                    available_table = Table.objects.filter(number_of_people=number_of_people, is_available=True).first()
                    if available_table:
                        reservation = Reservation.objects.create(user=user, table=available_table,
                                                                 number_of_people=number_of_people,
                                                                 date=date, start_time=start_time,
                                                                 end_time=end_time, name=name, email=email)
                        reservation_url = f'/reservation/{reservation.id}/'
                        return redirect(reservation_url)
                    else:
                        messages.error(request, 'No available table for the specified number of people.')
                        return redirect('make_reservation')
        else:
            messages.error(request, 'Invalid form data. Please check your input.')
            return redirect('make_reservation')
    else:
        form = ReservationForm()
        return render(request, 'make_reservation.html', {'form': form})





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




@login_required
def update_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id, user=request.user)
        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                form.save()
                reservation.table.is_available = True  
                reservation.table.save()
                messages.success(request, 'Reservation updated successfully.')
                return redirect('user_reservations')
        else:
            form = ReservationForm(instance=reservation)
    except Reservation.DoesNotExist:
        messages.error(request, 'Reservation does not exist or you are not authorized to update it.')
        return redirect('home')

    return render(request, 'update_reservation.html', {'form': form})


