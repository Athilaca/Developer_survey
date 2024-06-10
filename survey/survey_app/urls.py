from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name='survey'),
    path('survey',views.survey_view,name='survey'),
    path('success',views.success,name='success')
]