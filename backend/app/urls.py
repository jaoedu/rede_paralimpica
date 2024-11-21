from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.IndexView.as_view(), name="index"
    ),  # Página inicial com opções de cadastro e login
    path("home/", views.HomeView.as_view(), name="home"),  # Página home com notícias
    path(
        "atletas/", views.AthleteListView.as_view(), name="athlete_list"
    ),  # Lista de atletas
    path(
        "atletas/<int:pk>/", views.AthleteDetailView.as_view(), name="athlete_detail"
    ),  # Detalhes do atleta
    path(
        "atletas/criar/", views.CreateAthleteView.as_view(), name="create_athlete"
    ),  # Cadastro de atleta
    path(
        "atletas/<int:pk>/editar/",
        views.AthleteUpdateView.as_view(),
        name="athlete_update",
    ),  # Edição de atleta
    path(
        "atletas/<int:pk>/excluir/",
        views.AthleteDeleteView.as_view(),
        name="athlete_delete",
    ),  # Exclusão de atleta
    path(
        "treinadores/", views.CoachListView.as_view(), name="coach_list"
    ),  # Lista de treinadores
    path(
        "treinadores/<int:pk>/", views.CoachDetailView.as_view(), name="coach_detail"
    ),  # Detalhes do treinador
    path(
        "treinadores/criar/", views.CreateCoachView.as_view(), name="create_coach"
    ),  # Cadastro de treinador
    path(
        "treinadores/<int:pk>/editar/",
        views.CoachUpdateView.as_view(),
        name="coach_update",
    ),  # Edição de treinador
    path(
        "treinadores/<int:pk>/excluir/",
        views.CoachDeleteView.as_view(),
        name="coach_delete",
    ),  # Exclusão de treinador
    path(
        "competicoes/", views.CompetitionListView.as_view(), name="competition_list"
    ),  # Lista de competições
    path(
        "calendario-competicoes/",
        views.EventCalendarView.as_view(),
        name="competition_calendar",
    ),

    path(
        "competicoes/<int:pk>/",
        views.CompetitionDetailView.as_view(),
        name="competition_detail",
    ),  # Detalhes da competição
    path(
        "competicoes/criar/",
        views.CompetitionCreateView.as_view(),
        name="competition_create",
    ),  # Cadastro de competição
    path(
        "competicoes/<int:pk>/editar/",
        views.CompetitionUpdateView.as_view(),
        name="competition_update",
    ),  # Edição de competição
    path(
        "competicoes/<int:pk>/excluir/",
        views.CompetitionDeleteView.as_view(),
        name="competition_delete",
    ),  # Exclusão de competição
    path(
        "noticias/", views.NewsListView.as_view(), name="news_list"
    ),  # Lista de notícias
    path(
        "noticias/<int:pk>/", views.NewsDetailView.as_view(), name="news_detail"
    ),  # Detalhes da notícia
    path(
        "noticias/criar/", views.NewsCreateView.as_view(), name="news_create"
    ),  # Cadastro de notícia
    path(
        "noticias/<int:pk>/editar/", views.NewsUpdateView.as_view(), name="news_update"
    ),  # Edição de notícia
    path(
        "noticias/<int:pk>/excluir/", views.NewsDeleteView.as_view(), name="news_delete"
    ),  # Exclusão de notícia
    path(
        "patrocinadores/", views.SponsorListView.as_view(), name="sponsor_list"
    ),  # Lista de patrocinadores
    path(
        "patrocinadores/criar/",
        views.CreateSponsorView.as_view(),
        name="create_sponsor",
    ),  # Cadastro de patrocinador
    path(
        "patrocinadores/<int:pk>/editar/",
        views.SponsorUpdateView.as_view(),
        name="sponsor_update",
    ),  # Edição de patrocinador
    path(
        "patrocinadores/<int:pk>/excluir/",
        views.SponsorDeleteView.as_view(),
        name="sponsor_delete",
    ),  # Exclusão de patrocinador
    path("feed/", views.FeedView.as_view(), name="feed"),  # Feed de postagens
    path(
        "posts/criar/", views.CreatePostView.as_view(), name="create_post"
    ),  # Cadastro de post
    path(
        "posts/<int:post_id>/comentar/",
        views.CommentView.as_view(),
        name="comment_post",
    ),  # Comentário em post
    path(
        "posts/<int:post_id>/curtir/", views.LikePostView.as_view(), name="like_post"
    ),  # Curtir post
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/editar/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/excluir/", views.PostDeleteView.as_view(), name="post_delete"),
    path(
        "comentarios/<int:pk>/editar/",
        views.CommentUpdateView.as_view(),
        name="comment_update",
    ),
    path(
        "comentarios/<int:pk>/excluir/",
        views.CommentDeleteView.as_view(),
        name="comment_delete",
    ),
    path("login/", views.login_view, name="login"),  # Página de login
    path("logout/", views.logout_view, name="logout"),  # Página de logout
]
