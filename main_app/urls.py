from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:entry_id>/', views.detail, name='detail'),
    path('zapis-na_to/', views.tec_servise, name='tec_service'),
    path('zapis-na-test-drive/<int:car_id>/', views.test_drive, name='test_drive'),
    path('o-kompanii/', views.about_company, name='about_company'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', LoginView.as_view(template_name='main_app/login.html'), name='login'),
    path('register/', views.registration, name='register'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('personal-account/', PasswordChangeView.as_view(template_name='main_app/personal_account.html', success_url=reverse_lazy('home')), name='personal_account'),
    path('add/', views.add_new_entry, name='add'),
    path('all_clients/', views.all_clients, name='all_clients'),
    path('zayavki_na_test-drive/', views.test_drive_requests, name='test_drive_requests'),
    path('zapisi_na_to/', views.tec_servise_requests, name='tec_servise_requests'),
    path('page_ist_developed/', views.page_ist_developed, name='page_ist_developed')
]