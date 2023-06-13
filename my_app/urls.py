from django.urls import path
from my_app.views import about, login, contact, add_form, index_my_app

urlpatterns = [
    path('', index_my_app),
    path('about/', about),
    path('login/', login),
    path('contact/<int:id>', contact),
    path('add_form', add_form),
]