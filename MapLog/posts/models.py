from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=50)
    pick_date = models.DateField()
    create_date = models.DateField(auto_now=True)
    music = models.CharField(max_length=100)
    mood = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title