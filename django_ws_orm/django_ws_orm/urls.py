from django.urls import path
from orm import views

urlpatterns = [
    path('', views.start_page),
    path('users', views.get_users_profile),
    path('user/<int:id>', views.get_delete_put_user_profile),
    path('user', views.post_user_profile),
]