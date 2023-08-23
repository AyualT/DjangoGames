from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPublishersView.as_view(), name='publishers_list'),
    path('<int:pk>/', views.PublisherView.as_view(), name='publisher_detail'),
    path('new', views.publisher_new, name='publisher_new'),
    path('edit/<int:pk>', views.publisher_edit, name='publisher_edit'),
]
