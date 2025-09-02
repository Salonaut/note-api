from django.db import models
from django.core.validators import MaxLengthValidator


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tittle",
                             help_text="Enter title")
    content = models.TextField(validators=[MaxLengthValidator(10000)],
                               verbose_name="Content",
                               help_text="Enter description for note")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation') # auto_now_add - set date when create obj
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Date of update') # auto_add - update date everytime we use save() with obj

    class Meta:
        verbose_name = "Notes"
        verbose_name_plural = "Notes"
        ordering = ['-created_at']

    def str(self):
        return self.title
