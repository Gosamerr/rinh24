from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models import ManyToManyField
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    your_courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class Course(models.Model):
    topic = models.CharField(max_length=100)
    teacher = models.ManyToManyField(User)
    price = models.IntegerField()

    steps = models.ManyToManyField('Lesson')

    def __str__(self):
        return self.topic

class Lesson(models.Model):

    video = models.FileField(upload_to='videos/')
    practice = models.FileField(upload_to='practices/')

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name