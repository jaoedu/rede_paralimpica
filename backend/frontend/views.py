from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from app.models import News, Athlete, Competition, Coach, Sponsor, Post, Comment, Like
from app.forms import PostForm, CommentForm


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


class CompetitionListView(ListView):
    model = Competition
    template_name = "pages/competition_list.html"
    context_object_name = "competitions"


class CompetitionDetailView(DetailView):
    model = Competition
    template_name = "pages/competition_detail.html"


class NewsListView(ListView):
    model = News
    template_name = "pages/news_list.html"
    context_object_name = "news"
    ordering = "-publication_date"


class NewsDetailView(DetailView):
    model = News
    template_name = "pages/news_detail.html"
    context_object_name = "article"


class SponsorListView(ListView):
    model = Sponsor
    template_name = "pages/sponsor_list.html"
    context_object_name = "sponsors"


class CoachListView(ListView):
    model = Coach
    template_name = "pages/coach_list.html"
    context_object_name = "coaches"


class CoachDetailView(DetailView):
    model = Coach
    template_name = "pages/coach_detail.html"


class FeedView(ListView):
    model = Post
    template_name = "pages/feed.html"
    context_object_name = "posts"
    ordering = "-publication_date"


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "pages/create_post.html"
    success_url = reverse_lazy("feed")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "pages/comment.html"

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_id"])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.kwargs["post_id"]})


class PostDetailView(DetailView):
    model = Post
    template_name = "pages/post_detail.html"
    context_object_name = "post"


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect("post_detail", pk=post_id)
