from django.db import models

# Create your models here.


class Artist(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=64)
    url = models.URLField()


class Painting(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=64)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name="paintings"
    )
    image_url = models.URLField()


class CardStack(models.Model):
    artists = models.ManyToManyField(Artist)
    study_paintings = models.ManyToManyField(Painting, related_name="study_paintings")
    test_paintings = models.ManyToManyField(Painting, related_name="test_paintings")
