from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingView, basename='booking')

urlpatterns += router.urls