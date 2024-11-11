from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    is_athlete = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures", null=True, blank=True
    )

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.username


class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="athlete")
    birth_date = models.DateField()
    functional_classification = models.CharField(max_length=50)
    modalities = models.ManyToManyField("Modality", related_name="athletes")
    competition_history = models.TextField(blank=True)
    personal_records = models.TextField(blank=True)
    photos = models.ManyToManyField("Photo", related_name="athletes", blank=True)


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="coach")
    specialization = models.CharField(max_length=100)
    trained_athletes = models.ManyToManyField(
        Athlete, related_name="coaches", blank=True
    )
    experience = models.TextField(blank=True)


class Modality(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)
    modalities = models.ManyToManyField(Modality, related_name="competitions")
    competition_results = models.ManyToManyField(
        Athlete, through="Result", related_name="competitions"
    )

    def __str__(self):
        return self.name


class Result(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, related_name="competition_results"
    )
    competition = models.ForeignKey(
        Competition, on_delete=models.CASCADE, related_name="results"
    )
    time = models.TimeField()
    placement = models.IntegerField()
    record = models.BooleanField(default=False)


class Record(models.Model):
    athlete = models.ForeignKey(
        Athlete, on_delete=models.CASCADE, related_name="records"
    )
    modality = models.ForeignKey(
        Modality, on_delete=models.CASCADE, related_name="records"
    )
    classification = models.CharField(max_length=50)
    time = models.TimeField()
    type = models.CharField(max_length=50)


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")

    def __str__(self):
        return self.title


class Sponsor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="sponsors")
    description = models.TextField(blank=True)
    sponsorship_level = models.CharField(max_length=50)
    sponsored_competitions = models.ManyToManyField(
        Competition, related_name="sponsors_competition", blank=True
    )
    sponsored_athletes = models.ManyToManyField(
        Athlete, related_name="sponsors_athlete", blank=True
    )
    sponsored_news = models.ManyToManyField(
        News, related_name="sponsors_news", blank=True
    )

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to="photos")
    description = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photos")


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
