from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("atletas/", views.AthleteListView.as_view(), name="athlete_list"),
    path("atletas/<int:pk>/", views.AthleteDetailView.as_view(), name="athlete_detail"),
    path("atletas/criar/", views.CreateAthleteView.as_view(), name="create_athlete"),
    path(
        "atletas/<int:pk>/editar/",
        views.AthleteUpdateView.as_view(),
        name="athlete_update",
    ),
    path(
        "atletas/<int:pk>/excluir/",
        views.AthleteDeleteView.as_view(),
        name="athlete_delete",
    ),
    path("treinadores/", views.CoachListView.as_view(), name="coach_list"),
    path("treinadores/<int:pk>/", views.CoachDetailView.as_view(), name="coach_detail"),
    path("treinadores/criar/", views.CreateCoachView.as_view(), name="create_coach"),
    path(
        "treinadores/<int:pk>/editar/",
        views.CoachUpdateView.as_view(),
        name="coach_update",
    ),
    path(
        "treinadores/<int:pk>/excluir/",
        views.CoachDeleteView.as_view(),
        name="coach_delete",
    ),
    path("competicoes/", views.CompetitionListView.as_view(), name="competition_list"),
    path(
        "competicoes/<int:pk>/",
        views.CompetitionDetailView.as_view(),
        name="competition_detail",
    ),
    path(
        "competicoes/criar/",
        views.CompetitionCreateView.as_view(),
        name="competition_create",
    ),
    path(
        "competicoes/<int:pk>/editar/",
        views.CompetitionUpdateView.as_view(),
        name="competition_update",
    ),
    path(
        "competicoes/<int:pk>/excluir/",
        views.CompetitionDeleteView.as_view(),
        name="competition_delete",
    ),
    path(
        "competicoes/calendario/",
        views.CompetitionCalendarView.as_view(),
        name="competition_calendar",
    ),
    path("noticias/", views.NewsListView.as_view(), name="news_list"),
    path("noticias/<int:pk>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("noticias/criar/", views.NewsCreateView.as_view(), name="news_create"),
    path(
        "noticias/<int:pk>/editar/", views.NewsUpdateView.as_view(), name="news_update"
    ),
    path(
        "noticias/<int:pk>/excluir/", views.NewsDeleteView.as_view(), name="news_delete"
    ),
    path("patrocinadores/", views.SponsorListView.as_view(), name="sponsor_list"),
    path(
        "patrocinadores/criar/",
        views.CreateSponsorView.as_view(),
        name="create_sponsor",
    ),
    path(
        "patrocinadores/<int:pk>/editar/",
        views.SponsorUpdateView.as_view(),
        name="sponsor_update",
    ),
    path(
        "patrocinadores/<int:pk>/excluir/",
        views.SponsorDeleteView.as_view(),
        name="sponsor_delete",
    ),
    path("feed/", views.FeedView.as_view(), name="feed"),
    path("posts/criar/", views.CreatePostView.as_view(), name="create_post"),
    path(
        "posts/<int:post_id>/comentar/",
        views.CommentView.as_view(),
        name="comment_post",
    ),
    path("posts/<int:post_id>/curtir/", views.LikePostView.as_view(), name="like_post"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
