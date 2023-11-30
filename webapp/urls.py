from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('logout-user', views.logout_user, name="logout-user"),
    #CRUD
    path('dashboard', views.dashboard, name="dashboard"),
    path('create-record', views.create_record, name="create-record"),
    path('update-record/<int:pk>', views.update_record, name="update-record"),
    path('record/<int:pk>', views.single_record, name="record"),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
]