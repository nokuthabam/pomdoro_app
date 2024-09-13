from django import forms
from .models import Note, Image


class NoteForm(forms.ModelForm):
    """
    A class used to represent a form for a note
    Attributes:
        content (TextField): The content of the note
    """
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

    class Meta:
        """
        A class used to represent the metadata of the form
        """
        model = Note
        fields = ['content']


class ImageForm(forms.ModelForm):
    """
    A class used to represent a form for an image
    Attributes:
        image (ImageField): The image file
    """

    class Meta:
        """
        A class used to represent the metadata of the form
        """
        model = Image
        fields = ['image']
