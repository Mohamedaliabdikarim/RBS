from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import Menu
from .forms import SignUpForm
from .models import Review





def home(request):
    reviews = Review.objects.all()
    return render(request, 'home.html',{'reviews': reviews})



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in.')
            return redirect('menu')
        else:
            messages.error(request, 'There was an error. Please try again.')
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def menu_list(request):
    menu_list = Menu.objects.all()
    context = {'menu_list': menu_list, }
    return render(request, 'menu.html',context)

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def add_review(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        # Perform basic validation
        if not author or not content or not rating:
            # If any of the fields are missing, return with an error message
            return render(request, 'add_review.html', {'error_message': 'All fields are required.'})

        # Convert rating to integer
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                # Rating should be between 1 and 5
                return render(request, 'add_review.html', {'error_message': 'Rating should be between 1 and 5.'})
        except ValueError:
            # If rating is not a valid integer, return with an error message
            return render(request, 'add_review.html', {'error_message': 'Rating should be a number.'})

        # Create the review
        try:
            Review.objects.create(author=author, content=content, rating=rating)
            # Redirect to the review list after successful creation
            return redirect('home')
        except Exception as e:
            # If any other error occurs during creation, return with an error message
            return render(request, 'add_review.html', {'error_message': f'An error occurred: {str(e)}'})

    # If request method is not POST, render the form
    return render(request, 'add_review.html')

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})


