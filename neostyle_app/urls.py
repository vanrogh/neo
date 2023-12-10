# neostyle_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView
from .views import index, architecture, comerc_interior, interior_design, portfolio, employee_dashboard, change_status, delete_request

urlpatterns = [
    path('index/', index, name='index'),
    path('architecture/', architecture, name='architecture'),
    path('comerc-interior/', comerc_interior, name='comerc_interior'),
    path('interior-design/', interior_design, name='interior_design'),
    path('portfolio/', portfolio, name='portfolio'),
    path('employee_dashboard/', employee_dashboard, name='employee_dashboard'),
    path('login/', LoginView.as_view(template_name='neostyle_app/login.html'), name='login'),

    path('accounts/profile/', employee_dashboard, name='employee_dashboard'),
    path('change_status/<int:request_id>/', change_status, name='change_status'),
    path('delete_request/<int:request_id>/', delete_request, name='delete_request'),
]

