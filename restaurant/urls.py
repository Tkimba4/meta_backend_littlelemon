from django.urls import path
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.index, name='home'),
    path('test/', views.myView, name='test-view'),
    path('menu/', views.MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),
]

router = routers.DefaultRouter()
router.register(r'bookings', views.BookingView, basename='booking')

urlpatterns += router.urls