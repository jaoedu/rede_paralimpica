from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy,reverse
from app.models import News, Athlete, Competition, Coach, Sponsor, Post,Like, Comment, User
from app.forms import (
    PostForm,
    CommentForm,
    AthleteForm,
    CoachForm,
    CompetitionForm,
    NewsForm,
    SponsorForm,
    LoginForm,
)
from django.utils import timezone
from django.contrib.auth import login, logout


# Index View
class IndexView(TemplateView):
    template_name = "pages/index.html"


class HomeView(ListView):
    model = News
    template_name = "pages/home.html"
    context_object_name = "latest_news"
    ordering = "-publication_date"
    paginate_by = 5


# Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "pages/login.html", {"form": form})


# Logout View
def logout_view(request):
    logout(request)
    return redirect("home")


# Athlete Views
class AthleteListView(ListView):
    model = Athlete
    template_name = "pages/athlete_list.html"
    context_object_name = "athletes"


class AthleteDetailView(DetailView):
    model = Athlete
    template_name = "pages/athlete_detail.html"


class CreateAthleteView(CreateView):
    model = Athlete
    form_class = AthleteForm
    template_name = "pages/create_athlete.html"
    success_url = reverse_lazy("athlete_list")

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        form.instance.user = user
        form.instance.user.is_athlete = True
        form.instance.user.save()
        return super().form_valid(form)


class AthleteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Athlete
    form_class = AthleteForm
    template_name = "pages/create_athlete.html"
    success_url = reverse_lazy("athlete_list")

    def test_func(self):
        athlete = self.get_object()
        return self.request.user == athlete.user


class AthleteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Athlete
    template_name = "pages/athlete_confirm_delete.html"
    success_url = reverse_lazy("athlete_list")

    def test_func(self):
        athlete = self.get_object()
        return self.request.user == athlete.user


# Coach Views
class CoachListView(ListView):
    model = Coach
    template_name = "pages/coach_list.html"
    context_object_name = "coaches"


class CoachDetailView(DetailView):
    model = Coach
    template_name = "pages/coach_detail.html"


class CreateCoachView(CreateView):
    model = Coach
    form_class = CoachForm
    template_name = "pages/create_coach.html"
    success_url = reverse_lazy("coach_list")

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        form.instance.user = user
        form.instance.user.is_coach = True
        form.instance.user.save()
        return super().form_valid(form)


class CoachUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Coach
    form_class = CoachForm
    template_name = "pages/create_coach.html"
    success_url = reverse_lazy("coach_list")

    def test_func(self):
        coach = self.get_object()
        return self.request.user == coach.user


class CoachDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Coach
    template_name = "pages/coach_confirm_delete.html"
    success_url = reverse_lazy("coach_list")

    def test_func(self):
        coach = self.get_object()
        return self.request.user == coach.user


# Competition Views
class CompetitionListView(ListView):
    model = Competition
    template_name = "pages/competition_list.html"
    context_object_name = "competitions"


class CompetitionDetailView(DetailView):
    model = Competition
    template_name = "pages/competition_detail.html"


class CompetitionCreateView(LoginRequiredMixin, CreateView):
    model = Competition
    form_class = CompetitionForm
    template_name = "pages/create_competition.html"
    success_url = reverse_lazy("competition_calendar")


class CompetitionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    form_class = CompetitionForm
    template_name = "pages/create_competition.html"
    success_url = reverse_lazy("competition_list")

    def test_func(self):
        competition = self.get_object()
        return self.request.user.is_staff


class CompetitionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Competition
    template_name = "pages/competition_confirm_delete.html"
    success_url = reverse_lazy("competition_list")

    def test_func(self):
        competition = self.get_object()
        return self.request.user.is_staff


class EventCalendarView(ListView):
    model = Competition
    template_name = "pages/competition_calendar.html"
    context_object_name = "competitions"

    def get_queryset(self):
        # Filtra competições futuras
        return Competition.objects.filter(date__gte=timezone.now()).order_by("date")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Prepara os dados das competições para o calendário
        context["events"] = [
            {
                "title": competition.name,
                "start": competition.date.isoformat(),  # Formato ISO para o FullCalendar
                "location": competition.location,
                "description": competition.description,
                "event_type": competition.event_type,
            }
            for competition in context["competitions"]
        ]
        return context


# News Views
class NewsListView(ListView):
    model = News
    template_name = "pages/news_list.html"
    context_object_name = "news"
    ordering = "-publication_date"


class NewsDetailView(DetailView):
    model = News
    template_name = "pages/news_detail.html"
    context_object_name = "article"


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = "pages/create_news.html"
    success_url = reverse_lazy("news_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = "pages/create_news.html"
    success_url = reverse_lazy("news_list")

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = "pages/news_confirm_delete.html"
    success_url = reverse_lazy("news_list")

    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author


# Sponsor Views
class SponsorListView(ListView):
    model = Sponsor
    template_name = "pages/sponsor_list.html"
    context_object_name = "sponsors"


class CreateSponsorView(CreateView):
    model = Sponsor
    form_class = SponsorForm
    template_name = "pages/create_sponsor.html"
    success_url = reverse_lazy("sponsor_list")

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        form.instance.user = user
        form.instance.user.is_sponsor = True
        form.instance.user.save()
        return super().form_valid(form)


class SponsorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Sponsor
    form_class = SponsorForm
    template_name = "pages/create_sponsor.html"
    success_url = reverse_lazy("sponsor_list")

    def test_func(self):
        sponsor = self.get_object()
        return self.request.user.is_staff


class SponsorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Sponsor
    template_name = "pages/sponsor_confirm_delete.html"
    success_url = reverse_lazy("sponsor_list")

    def test_func(self):
        sponsor = self.get_object()
        return self.request.user.is_staff


# Feed Views
class FeedView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "pages/feed.html"
    context_object_name = "posts"
    ordering = "-publication_date"


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "pages/create_post.html"
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["comment_form"] = CommentForm()
        context["liked"] = Like.objects.filter(
            post=self.object, user=self.request.user
        ).exists()
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "pages/create_post.html"  # Reutilize o template de criação
    success_url = reverse_lazy("feed")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "pages/post_confirm_delete.html"
    success_url = reverse_lazy("feed")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "pages/comment_edit.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "pages/comment_confirm_delete.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "pages/comment.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, id=self.kwargs["post_id"])
        return context

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, id=self.kwargs["post_id"])
        form.instance.author = self.request.user
        return super().form_valid(form)


class LikePostView(LoginRequiredMixin, CreateView):
    model = Like
    fields = []

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, id=self.kwargs["post_id"])
        form.instance.user = self.request.user
        like = Like.objects.filter(post=form.instance.post, user=form.instance.user)
        if like.exists():
            like.delete()
        else:
            form.save()
        return redirect("post_detail", pk=self.kwargs["post_id"])
