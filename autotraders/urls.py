from django.urls import path
from autotraders import views

urlpatterns = [
    path("autotraders/", views.AutotraderList().as_view()),
    path("autotraders/<int:pk>/", views.AutotraderDetails().as_view()),
]
