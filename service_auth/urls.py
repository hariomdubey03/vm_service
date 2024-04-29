from django.urls import path
from .views import Authentication


urlpatterns = [
    path(
        "api/<str:slug>",
        Authentication.as_view(),
        name="authentication",
    )
]
