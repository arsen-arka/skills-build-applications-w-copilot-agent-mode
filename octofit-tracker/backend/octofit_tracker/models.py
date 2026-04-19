from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    reps = models.IntegerField(null=True, blank=True)
    distance_km = models.FloatField(null=True, blank=True)
    duration_min = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.activity}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggested_for = models.JSONField(default=list)
    def __str__(self):
        return self.name
