from django.urls import path
from . import views

app_name = 'bulletin'

urlpatterns = [
    path('', views.home, name='home'),
    path('board/<int:board_id>/', views.board, name='board'),
    path('add_board/', views.add_board, name='add_board'),
    path('add_note/<int:board_id>/', views.add_note, name='add_note'),
    path('add_image/<int:board_id>/', views.add_image, name='add_image'),
    path('update_position/<int:item_id>/',
         views.update_position, name='update_position'),
    # delete notes
    path('delete_note/<int:note_id>/',
         views.delete_note, name='delete_note'),
    # delete images
    path('delete_image/<int:image_id>/',
         views.delete_image, name='delete_image'),
    # delete board
    path('delete_board/<int:board_id>/',
         views.delete_board, name='delete_board'),
]