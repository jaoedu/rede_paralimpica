from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .models import (
    News,
    Athlete,
    Competition,
    Coach,
    Sponsor,
    Post,
    Comment,
    Like,
    User,
)
from .forms import (
    PostForm,
    CommentForm,
    AthleteForm,
    CoachForm,
    CompetitionForm,
    NewsForm,
    SponsorForm,
    LoginForm,
)


class HomeView(ListView):
    model = News
    template_name = "pages/home.html"
    context_object_name = "latest_news"
    ordering = "-publication_date"
    paginate_by = 5


class AthleteListView(ListView):
    model = Athlete
    template_name = "pages/athlete_list.html"
    context_object_name = "athletes"


class AthleteDetailView(DetailView):
    model = Athlete
    template_name = "pages/athlete_detail.html"


class CreateAthleteView(LoginRequiredMixin, CreateView):
    model = Athlete
    form_class = AthleteForm
    template_name = "pages/create_athlete.html"
    success_url = reverse_lazy("athlete_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
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


class CoachListView(ListView):
    model = Coach
    template_name = "pages/coach_list.html"
    context_object_name = "coaches"


class CoachDetailView(DetailView):
    model = Coach
    template_name = "pages/coach_detail.html"


class CreateCoachView(LoginRequiredMixin, CreateView):
    model = Coach
    form_class = CoachForm
    template_name = "pages/create_coach.html"
    success_url = reverse_lazy("coach_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
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
    success_url = reverse_lazy("competition_list")


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


class SponsorListView(ListView):
    model = Sponsor
    template_name = "pages/sponsor_list.html"
    context_object_name = "sponsors"


class CreateSponsorView(LoginRequiredMixin, CreateView):
    model = Sponsor
    form_class = SponsorForm
    template_name = "pages/create_sponsor.html"
    success_url = reverse_lazy("sponsor_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
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


class CommentView(LoginRequiredMixin, CreateView):
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


class LoginView(LoginView):
    template_name = "pages/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")


class LogoutView(LogoutView):
    next_page = "home"


class CompetitionCalendarView(ListView):
    model = Competition
    template_name = "pages/competition_calendar.html"
    context_object_name = "competitions"


class LoginView(LoginView):
    template_name = "pages/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")
