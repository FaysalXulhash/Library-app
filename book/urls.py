from django.urls import path
from .views import createBook, viewBook, deleteBook, updatebook
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', createBook, name='add-book'),
    path('viewbooks/', viewBook, name='view-book'),
    path('delete/book/<int:id>/',deleteBook, name='delete-book'),
    path('update/book/<int:id>', updatebook, name='update-book'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)