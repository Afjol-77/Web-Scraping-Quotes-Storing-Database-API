from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateQuotesList.as_view()),
    path('',ReadQuotesList.as_view()),
    path('<int:pk>/', RetrieveQuotesList.as_view()),
    path('delete/<int:pk>', DeleteQuotesList.as_view())
]