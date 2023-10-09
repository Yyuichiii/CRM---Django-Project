from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name=''),
    path('register/',views.register, name='register'),
    path('login/',views.login_, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('create/',views.create_record, name='create'),
    path('delete/<int:pk>',views.delete_record, name='delete'),
    path('update/<int:pk>',views.update_record, name='update'),
    path('view/<int:pk>',views.view_record, name='view'),
]


