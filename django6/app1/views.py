# app1/views.py
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = StudentRegistrationForm()
    return render(request, 'app1/register.html', {'form': form})
