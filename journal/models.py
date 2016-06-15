from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=64)
    icon = models.CharField(max_length=64)
    color = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Entry(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    skills = models.ManyToManyField(Skill, blank=True)
    content = models.TextField()

    def __str__(self):
        return "{}: {}".format(self.date, self.title)


class Resource(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    entry = models.ForeignKey(Entry)

    def __str__(self):
        return self.name
