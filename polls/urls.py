from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from .views import (
    PollViewSet,
    ChoiceList,
    CreateVote,
    UserCreate,
    LoginView,
)
router = DefaultRouter()
router.register('polls', PollViewSet, basename = 'polls')

urlpatterns = [
    path("login/", views.obtain_auth_token, name = "login"),
    path("users/", UserCreate.as_view(), name = 'user_create'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name = 'choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name = 'create_vote'),
]
urlpatterns += router.urls