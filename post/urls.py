from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, \
    PostCommentListView, PostCommentCreateView, PostLikesView, CommentRetriveView, \
    CommentLikesView, PostLikeApiView, CommentLikeApiView

urlpatterns = [
    path('list/', PostListApiView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('<uuid:pk>/likes/', PostLikesView.as_view()),
    path('<uuid:pk>/create-delete-like/', PostLikeApiView.as_view()),
    path('<uuid:pk>/comments/', PostCommentListView.as_view()),
    path('comments/<uuid:pk>/', CommentRetriveView.as_view()),
    path('comments/<uuid:pk>/likes/', CommentLikesView.as_view()),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view()),
    path('comments/<uuid:pk>/create-delete-like/', CommentLikeApiView.as_view()),
]
