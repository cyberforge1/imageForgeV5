from django.db import models

# Create your models here.
class Prompt(models.Model):
    '''A prompt generated for the user'''
    text_field = models.TextField()  # Rename the field to avoid conflicts
    date_added = models.DateTimeField(auto_now_add=True)
    
    def get_text(self):
        return self.text_field
    
    def get_datetime(self):
        return self.date_added
    
    
class Image(models.Model):
    text_field = models.TextField()
    datetime_field = models.DateTimeField(auto_now_add=True)
    image_field = models.ImageField(upload_to='images/')

    def get_text(self):
        return self.text_field

    def get_datetime(self):
        return self.datetime_field

    def get_image_url(self):
        if self.image_field:
            return self.image_field.url
        return None
    