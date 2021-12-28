from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.CreateVideo.as_view(), name='video-create'),
    path('view_movie/<int:id>', views.view_movie, name='view_movie'),
    path('<int:pk>/edit', views.UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', views.DeleteVideo.as_view(), name="video-delete"),
    path('members/', views.members, name='members'),

]