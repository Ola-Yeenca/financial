from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.index, name='index'),
    path('personal_finance_cal/', views.personal_finance_cal, name='personal_finance_cal'),
]
