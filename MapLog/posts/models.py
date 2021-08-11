from django.db import models
from django.db.models.fields import DecimalField


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    pick_date = models.DateField(null=True)
    create_date = models.DateField(auto_now=True, null=True)
    music = models.CharField(max_length=100, null=True)

    # mood 선택을 위한 모델
    MOOD_CHOICES = (
        # 앞: db에 저장, templates에 표시 / 뒤: admin에 저장
        ("happy", "happy"),
        ("soso", "soso"),
        ("sad", "sad"),
        ("angry", "angry"),
    )
    mood = models.CharField(max_length=5, choices=MOOD_CHOICES, null=True)

    description = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    # 위도, 경도에 대한 모델
    lat = models.CharField(max_length=50, null=True)
    lng = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.title)  # __str__오류 수정

    # def to_json(self):
    #     return {
    #         "title": self.title,
    #         "pick_date": self.pick_date,
    #         "create_date": self.create_date,
    #         "music": self.music,
    #         "mood": self.mood,
    #         "description": self.description,
    #         "image": self.image,
    #         "lat": self.lat,
    #         "lng": self.lng,
    #     }
