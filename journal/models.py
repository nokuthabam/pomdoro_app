from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class JournalEntry(models.Model):
    """
    A class used to represent a journal entry
    Attributes:
        title (CharField): The title of the entry
        date (DateField): The date of the entry
        created_at (DateTimeField): Sate and time the entry was created
        last_modified (DateTimeField): Date and time entry was last modified
        user (ForeignKey): The user who created the entry
    """
    title = models.CharField(max_length=200)
    body = models.TextField()  # For larger text fields
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='journal_entries', null=True)

    def __str__(self):
        """
        A function used to return the title of the entry
        """
        return self.title
