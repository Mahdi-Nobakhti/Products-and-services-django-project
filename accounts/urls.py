from django.urls import path 
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', Login, name='login' ),
    path('logout/', Logout, name='logout' ),
    path('signup/', Signup, name='signup' ),
    path('change-picture/', change_photo, name='change' ),
    path('change-default/', default_photo, name='default' ),
    path('delete-account/<int:userid>', delete, name='delete' ),

]