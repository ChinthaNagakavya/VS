from django.urls import path
from . import views

urlpatterns=[
   path('',views.display),
   path('one/<int:pk>',views.details,name='details'),
   path('edit/<int:jp>',views.update,name='edit'),
]