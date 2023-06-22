from django.urls import path
from . import views

urlpatterns = [
    path('calorie_calculator', views.calorie_calculator, name='calorie_calculator'),
    path('bmr_calculator', views.bmr_calculator, name='bmr_calculator'),
    path('tdee_calculator', views.tdee_calculator, name='tdee_calculator'),

]
