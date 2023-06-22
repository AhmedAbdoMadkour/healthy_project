from django.shortcuts import render

# Create your views here.
def calorie_calculator(request):
    return render(request, 'calorie_calculator.html')

def bmr_calculator(request):
    return render(request, 'bmr_calculator.html')

def tdee_calculator(request):
    return render(request, 'tdee_calculator.html')
