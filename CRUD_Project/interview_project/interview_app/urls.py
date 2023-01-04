from django.urls import path
from .views import Home,Add_User,DeleteUser
urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('add-user/', Add_User.as_view(),name='add-user'),
    path('delete-user/',DeleteUser.as_view(),name='delete-user')
]
