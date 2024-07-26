from django.urls import path
from . import views
from .views import Bookingsview, Menuview

urlpatterns = [
    path('', views.index, name='index'),
    path('bookings/', views.Bookingsview.as_view()),
    path('bookings/<int:pk>', views.SingleBookingsview.as_view()),
    path('menu/', views.Menuview.as_view()),
    path('menu/<int:pk>', views.SingleMenuview.as_view()),
]