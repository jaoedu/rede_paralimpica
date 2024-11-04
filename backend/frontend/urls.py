from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("atletas/", views.AthleteListView.as_view(), name="athlete_list"),
    path("atletas/<int:pk>/", views.AthleteDetailView.as_view(), name="athlete_detail"),
    path("competicoes/", views.CompetitionListView.as_view(), name="competition_list"),
    path(
        "competicoes/<int:pk>/",
        views.CompetitionDetailView.as_view(),
        name="competition_detail",
    ),
    path("noticias/", views.NewsListView.as_view(), name="news_list"),
    path("noticias/<int:pk>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("patrocinadores/", views.SponsorListView.as_view(), name="sponsor_list"),
    path("treinadores/", views.CoachListView.as_view(), name="coach_list"),
    path("treinadores/<int:pk>/", views.CoachDetailView.as_view(), name="coach_detail"),
    path("feed/", views.FeedView.as_view(), name="feed"),
    path("posts/create/", views.CreatePostView.as_view(), name="create_post"),
    path(
        "posts/<int:post_id>/comment/", views.CommentView.as_view(), name="comment_post"
    ),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:post_id>/like/", views.like_post, name="like_post"),
]
