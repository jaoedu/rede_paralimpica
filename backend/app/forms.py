from django import forms
from .models import Post, Comment, Athlete, Coach, Competition, News, Sponsor


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


# Forms para os outros modelos (se necessário):


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
        ]  # ou os campos que desejar


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = "__all__"  # ou especifique os campos


class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = "__all__"  # ou especifique os campos


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"  # ou especifique os campos


class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"  # ou especifique os campos
