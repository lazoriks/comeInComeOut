from django.urls import path
from .views import login_view, user_list_view, last_time_view, report_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('user_list/', user_list_view, name='user_list'),
    path('last_time/', last_time_view, name='last_time'),
    path('report/', report_view, name='report'),
]
