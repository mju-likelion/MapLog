from django.db import models



class Posts(models.Model):
    title = models.CharField(max_length=50, null=True)
    pick_date = models.DateField(null=True)
    create_date = models.DateField(auto_now=True, null=True)
    music = models.CharField(max_length=100, null=True)
    mood = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    def __str__(self):
        return str(self.title) #__str__오류 수정
