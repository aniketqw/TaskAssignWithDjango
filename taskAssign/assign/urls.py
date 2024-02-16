from django.urls import path
from . import views

urlpatterns=[
    path('',views.assign,name='assign'),
    # path('submit-form/', views.submit_form, name='submit_form'),
    
]