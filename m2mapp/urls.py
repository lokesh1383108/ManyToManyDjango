from django.urls import path
from . import views

urlpatterns=[
    path('', views.display_data , name='student_by_teacher'),
    path('certificate/<id>',views.certificate, name = 'certificate')

]
    
