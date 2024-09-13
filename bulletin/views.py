from django.shortcuts import render
from .models import BulletinBoard, Note, Image
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def home(request):
    """
    A function used to render the home page
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    bulletin_boards = BulletinBoard.objects.filter(user=request.user)
    return render(request, 'bulletin/home.html',
                  {'bulletin_boards': bulletin_boards, 'user': request.user})


@login_required
def board(request, board_id):
    """
    A function used to render a bulletin board
    Args:
        request (HttpRequest): The request object
        board_id (int): The id of the bulletin board
    Returns:
        HttpResponse: The response object
    """
    bulletin_board = BulletinBoard.objects.get(id=board_id)
    notes = Note.objects.filter(bulletin_board=bulletin_board)
    images = Image.objects.filter(bulletin_board=bulletin_board)
    return render(request, 'bulletin/board.html',
                  {'bulletin_board': bulletin_board,
                   'notes': notes,
                   'images': images})


@login_required
def add_board(request):
    """
    A function used to add a bulletin board
    Args:
        request (HttpRequest): The request object
    Returns:
        HttpResponse: The response object
    """
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        bulletin_board = BulletinBoard(title=title, description=description,
                                       user=request.user)
        bulletin_board.save()
        return render(request, 'bulletin/board.html',
                      {'bulletin_board': bulletin_board})
    return render(request, 'bulletin/add_board.html')


@login_required
def add_note(request, board_id):
    """
    A function used to add a note to a bulletin board
    Args:
        request (HttpRequest): The request object
        board_id (int): The id of the bulletin board
    Returns:
        HttpResponse: The response object
    """
    bulletin_board = BulletinBoard.objects.get(id=board_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.bulletin_board = bulletin_board
            note.save()
            return render(request, 'bulletin/board.html',
                          {'bulletin_board': bulletin_board})
    else:
        form = NoteForm()
    return render(request, 'bulletin/add_note.html', {'form': form})
