from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class BulletinBoard(models.Model):
    """
    A class used to represent a bulletin board
    Attributes:
        title (CharField): The title of the bulletin board
        description (TextField): The description of the bulletin board
        created_at (DateTimeField): The date board was created
        user (ForeignKey): The user who created the bulletin board
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='bulletin_boards', null=True)

    def __str__(self):
        """
        A function used to return the title of the bulletin board
        """
        return self.title


class Note(models.Model):
    """
    A class used to represent a note
    Attributes:
        content (TextField): The content of the note
        created_at (DateTimeField): The date the note was created
        last_modified (DateTimeField): The date the note was last modified
        bulletin_board (ForeignKey): The bulletin board the note belongs to
        position_x (IntegerField): The x position of the note on the board
        position_y (IntegerField): The y position of the note on the board
    """
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    bulletin_board = models.ForeignKey(BulletinBoard, on_delete=models.CASCADE,
                                       related_name='notes', null=True)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

    def __str__(self):
        """
        A function used to return the title of the note
        """
        return self.title


class Image(models.Model):
    """
    A class used to represent an image
    Attributes:
        image (ImageField): The image file
        created_at (DateTimeField): The date the image was created
        bulletin_board (ForeignKey): The bulletin board the image belongs to
        position_x (IntegerField): The x position of the image on the board
        position_y (IntegerField): The y position of the image on the board
    """
    image = models.ImageField(upload_to='media/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    bulletin_board = models.ForeignKey(BulletinBoard, on_delete=models.CASCADE,
                                       related_name='images', null=True)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

    def __str__(self):
        """
        A function used to return the image file name
        """
        return self.image.name
