from django.shortcuts import render, redirect
from .Forms import UserRegistrationForm


def index(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            student_number = form.cleaned_data['student_number']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            graduation_year = form.cleaned_data['graduation_year']
            date_joined = form.cleaned_data['date_joined']
            last_login = form.cleaned_data['last_login']
            degree = form.cleaned_data['degree']
            program = form.cleaned_data['program']
            image = form.cleaned_data['image']
            city = form.cleaned_data['city']
            CAPES_miles_points = form.cleaned_data['CAPES_miles_points']
            context = {'email': email, 'last_name': last_name, 'student_number': student_number, 'first_name':
                first_name, 'graduation_year': graduation_year, 'date_joined': date_joined, 'last_login':
                last_login, 'degree': degree, 'program': program, 'image': image, 'city': city, 'CAPES_miles_points': CAPES_miles_points}
            return render(request, 'ISworkshop/profile.html', context=context)
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'ISworkshop/index.html', context=context)
