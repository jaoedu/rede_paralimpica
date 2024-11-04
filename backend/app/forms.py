from django import forms
from .models import Post, Comment, Athlete, Coach, Competition, News, Sponsor


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = [
            "birth_date",
            "functional_classification",
            "modalities",
            "competition_history",
            "personal_records",
            "photos",
        ]


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ["specialization", "trained_athletes", "experience"]


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ["name", "date", "location", "modalities"]


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content"]


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ["name", "logo", "description", "sponsorship_level"]
