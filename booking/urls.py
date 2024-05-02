from django.urls import path
from . import views
from restaurant.views import login_user
from .views import reservation_detail




urlpatterns = [
    path('make_reservation/', views.make_reservation, name='make_reservation'),
   path('reservation/<int:reservation_id>/', views.reservation_detail, name='reservation_detail'),
   path('user_reservations/', views.user_reservations, name='user_reservations'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('reservation/<int:reservation_id>/update/', views.update_reservation, name='update_reservation'),
    


]
