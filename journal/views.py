from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import JournalEntryForm
from .forms import UserRegistrationForm
from .models import JournalEntry
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import get_object_or_404
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
    user_first_name = request.user
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
    current_date = timezone.now().strftime('%A %d. %B %Y')
    journal_entries = JournalEntry.objects\
        .filter(user=request.user).order_by('-created_at')
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
    return render(request, 'journal/create_entry.html',
                  {'form': form, 'current_date': current_date,
                   'journal_entries': journal_entries})


@login_required
def entry_detail(request, id):
    """
    A function used to render the detail page for a journal entry
    Args:
        request (HttpRequest): The request object
        entry_id (int): The id of the journal entry
    Returns:
        HttpResponse: The response object
    """
    entry = get_object_or_404(JournalEntry, pk=id)
    return render(request, 'journal/entry_detail.html', {'entry': entry})


@login_required
def edit_entry(request, id):
    """
    A function used to edit a journal entry
    Args:
        request (HttpRequest): The request object
        id (int): The id of the journal entry
    Returns:
        HttpResponse: The response object
    """
    entry = get_object_or_404(JournalEntry, id=id, user=request.user)

    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('journal:entry_detail', id=entry.id)
    else:
        form = JournalEntryForm(instance=entry)

    return render(request, 'journal/edit_entry.html',
                  {'form': form, 'entry': entry})


@login_required
def delete_entry(request, id):
    """
    A function used to delete a journal entry
    Args:
        request (HttpRequest): The request object
        id (int): The id of the journal entry
    Returns:
        HttpResponse: The response object
    """
    entry = get_object_or_404(JournalEntry, id=id, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('journal:home')
    return render(request, 'journal/delete_entry.html', {'entry': entry})
