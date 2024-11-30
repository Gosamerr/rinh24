from django.urls import path
from .views import home, profile, RegisterView, course, about, contacts

urlpatterns = [
    path('', home, name='users-home'),
    path('course/', course, name='users-course'),

    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
]
