from django.urls import path
from .views import StoreView, VisitCreateView


urlpatterns = [
    path('stores/', StoreView.as_view()),
    path('visits/create/', VisitCreateView.as_view())
]
