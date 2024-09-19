from django.shortcuts import render, redirect
from .models import BulletinBoard, Note, Image
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
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
            # Include notes and images in the context
            notes = Note.objects.filter(bulletin_board=bulletin_board)
            images = Image.objects.filter(bulletin_board=bulletin_board)
            return render(request, 'bulletin/board.html',
                          {'bulletin_board': bulletin_board,
                           'notes': notes, 'images': images})
    else:
        form = NoteForm()
    return render(request, 'bulletin/add_note.html',
                  {'form': form, 'bulletin_board': bulletin_board})


@login_required
def add_image(request, board_id):
    """
    A function used to add an image to a bulletin board
    Args:
        request (HttpRequest): The request object
        board_id (int): The id of the bulletin board
    Returns:
        HttpResponse: The response object
    """
    bulletin_board = BulletinBoard.objects.get(id=board_id)
    if request.method == 'POST':
        image = Image(image=request.FILES['image'],
                      bulletin_board=bulletin_board)
        image.save()
        # Include notes and images in the context
        notes = Note.objects.filter(bulletin_board=bulletin_board)
        images = Image.objects.filter(bulletin_board=bulletin_board)
        return render(request, 'bulletin/board.html',
                      {'bulletin_board': bulletin_board,
                       'notes': notes, 'images': images})
    return render(request, 'bulletin/add_image.html',
                  {'bulletin_board': bulletin_board})


@login_required
def update_position(request, item_id):
    """
    A function used to update the position of a note
    or image on a bulletin board
    Args:
        request (HttpRequest): The request object
        item_id (int): The id of the note or image
    Returns:
        HttpResponse: The response object
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        position_x = data.get('position_x', 0)
        position_y = data.get('position_y', 0)

        # Update Note or Image position based on the item ID
        try:
            note = Note.objects.get(id=item_id)
            note.position_x = position_x
            note.position_y = position_y
            note.save()
        except Note.DoesNotExist:
            try:
                image = Image.objects.get(id=item_id)
                image.position_x = position_x
                image.position_y = position_y
                image.save()
            except Image.DoesNotExist:
                return JsonResponse({'error': 'Item not found'}, status=404)

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def delete_image(request, image_id):
    """
    A function used to delete an image from a bulletin board.
    Args:
        request (HttpRequest): The request object
        image_id (int): The id of the image
    Returns:
        HttpResponse: The response object
    """
    image = Image.objects.get(id=image_id)
    bulletin_board = image.bulletin_board
    image.delete()

    # Redirect to the board view to refresh the board with updated images
    return redirect('bulletin:board', board_id=bulletin_board.id)


@login_required
def delete_note(request, note_id):
    """
    A function used to delete a note from a bulletin board.
    Args:
        request (HttpRequest): The request object
        note_id (int): The id of the note
    Returns:
        HttpResponse: The response object
    """
    note = Note.objects.get(id=note_id)
    bulletin_board = note.bulletin_board
    note.delete()

    # Redirect to the board view to refresh the board with updated notes
    return redirect('bulletin:board', board_id=bulletin_board.id)


@login_required
def delete_board(request, board_id):
    """
    A function used to delete a bulletin board
    Args:
        request (HttpRequest): The request object
        board_id (int): The id of the bulletin board
    Returns:
        HttpResponse: The response object
    """
    bulletin_board = BulletinBoard.objects.get(id=board_id)
    bulletin_board.delete()
    bulletin_boards = BulletinBoard.objects.filter(user=request.user)
    return render(request, 'bulletin/home.html',
                  {'bulletin_boards': bulletin_boards, 'user': request.user})
