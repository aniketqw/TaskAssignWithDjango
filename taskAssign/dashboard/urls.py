from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('details/',views.details,name='details'),
    path('task/',views.task,name='task'),
    path('modify/',views.modify,name='details'),
    path('rearrange/',views.rearrange,name='rearrange'),
    # path('submit-form/', views.submit_form, name='submit_form'),
    
]