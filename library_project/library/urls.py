from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', BookCreateView.as_view(), name='create-book'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail-book'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='update-book'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='delete-book'),

]
