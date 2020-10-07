from django.urls import path

from .views import OfficeView
urlpatterns = [
    path('', OfficeView.as_view())
]
