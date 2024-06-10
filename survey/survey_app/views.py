from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        request.session['name'] = name
        request.session['email'] = email
        return redirect('survey')
    return render(request, "home.html")


def survey_view(request):
    if request.method == 'POST':
        questions = {
            'Question 1': {'field_name': 'question_1', 'type': 'text'},
            'Question 2': {'field_name': 'question_2', 'type': 'radio'},
            'Question 3': {'field_name': 'question_3', 'type': 'radio'},
            'Question 4': {'field_name': 'question_4', 'type': 'radio'},
            'Question 5': {'field_name': 'question_5', 'type': 'radio'},
            'Question 6': {'field_name': 'question_6', 'type': 'radio'},
            'Question 7': {'field_name': 'question_7', 'type': 'radio'},
            'Question 8': {'field_name': 'question_8', 'type': 'text'},
            'Question 9': {'field_name': 'question_9', 'type': 'checkbox'},
            # Add more questions as needed
        }

        for question_text, data in questions.items():
            field_name = data['field_name']
            question_type = data['type']
            
            if question_type == 'text':
                answer_text = request.POST.get(field_name)
                Answer.objects.create(question_text=question_text, answer_text=answer_text)
            
            elif question_type == 'checkbox':
                selected_options = request.POST.getlist(field_name)
                answer_text = ', '.join(selected_options)  # Joining options with commas
                Answer.objects.create(question_text=question_text, answer_text=answer_text)
            
            elif question_type == 'radio':
                selected_option = request.POST.get(field_name)
                if selected_option:
                    Answer.objects.create(question_text=question_text, answer_text=selected_option)

            name = request.session.get('name')
            email = request.session.get('email')

            if not name or not email:
                return HttpResponse("User details not found. Please start the survey from the beginning.")

            student, created = Student.objects.get_or_create(name=name, email=email)        

        return redirect('success')  # Replace with your thank you page URL
    
    return render(request, 'survey.html')

def success(request):
    return render(request,'success.html')