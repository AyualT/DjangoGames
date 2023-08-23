from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllGamesView.as_view(), name='games_list'),
    path('<int:pk>',views.GameView.as_view(), name='game_detail'),
    path('new', views.game_new, name='game_new'),
    path('edit/<int:pk>', views.game_edit, name='game_edit'),
    path('review/<int:gid>/<int:uid>',views.create_review, name='create_review'),
    path('reviewlike/<int:gid>/<int:rid>/<int:uid>/', views.like_review, name='like_review'),
    path('reviewdislike/<int:gid>/<int:rid>/<int:uid>/', views.dislike_review, name='dislike_review'),
]
