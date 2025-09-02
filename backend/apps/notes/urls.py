from django.urls import path
from .views import NoteListCreateAPIView, NoteDetailAPIView

app_name = 'notes'

urlpatterns = [
    path('notes/', NoteListCreateAPIView.as_view()),
    path('notes/<int:pk>/', NoteDetailAPIView.as_view())
]