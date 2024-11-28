from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Athlete, Coach, Sponsor, Competition, News, Post, Comment


# Formulário de Registro de Usuário
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


# Formulário de Registro de Atleta
class AthleteForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Nome")
    username = forms.CharField(max_length=150, required=True, label="Nome de Usuário")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")
    photos = forms.ImageField(required=False, label="Foto")  # Campo para upload de foto

    class Meta:
        model = Athlete
        fields = [
            "birth_date",
            "functional_classification",
            "competition_history",
            "personal_records",
            "photos",
        ]


# Formulário de Registro de patrocinador
class SponsorForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Nome")
    username = forms.CharField(max_length=150, required=True, label="Nome de Usuário")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")

    class Meta:
        model = Sponsor
        fields = ["logo", "description", "sponsorship_level"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulário de Registro de treinador
class CoachForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label="Nome")
    username = forms.CharField(max_length=150, required=True, label="Nome de Usuário")
    password = forms.CharField(widget=forms.PasswordInput, required=True, label="Senha")

    class Meta:
        model = Coach
        fields = ["specialization", "experience"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Formulário de Login
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


# Formulário para Competição
class CompetitionForm(forms.ModelForm):
    class Meta:
       
            

        model = Competition
        fields = [
            "name",
            "date",
            "location",
            "description",
            "event_type",
        ]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),  # Para um seletor de data
            "description": forms.Textarea(
                attrs={"rows": 4}
            ),  # Para um campo de texto maior
        }



# Formulário para Postagem
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# Formulário para Notícias
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

# Formulário para Comentários
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Escreva seu comentário aqui...'})
