from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import JournalEntryForm
from .forms import UserRegistrationForm
from .models import JournalEntry
from django.contrib import messages
# Create your views here.


def signup(request):
    """
    A function used to sign up a user
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('journal:login')
        else:
            print(f"Form errors: {form.errors}")  # Debugging print statement
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    """
    A function used to log in a user
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('journal:home')
    return render(request, 'registration/login.html')


def user_logout(request):
    """
    A function used to log out a user
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    logout(request)
    return redirect('journal:login')


@login_required
def home(request):
    """
    A function used to render the home page
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    # Retrieve all journal entries
    user_first_name = request.user.first_name
    return render(request, 'journal/home.html',
                  {'user_first_name': user_first_name})


@login_required
def list_entries(request):
    """
    A function used to list all journal entries
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    # Retrieve all journal entries
    user_first_name = request.user.first_name
    entries = JournalEntry.objects.filter(user=request.user)
    return render(request, 'journal/list_entries.html',
                  {'entries': entries, 'user_first_name': user_first_name})


@login_required
def create_entry(request):
    """
    A function used to create a journal entry
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            # Create instance to add user to the entry
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('journal:home')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = JournalEntryForm()
    return render(request, 'journal/create_entry.html', {'form': form})
