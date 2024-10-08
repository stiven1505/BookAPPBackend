from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from books import views

#generar url Automaticas para el crud
router = routers.DefaultRouter ()
router.register(r'books', views.BooksView, 'books')

#lista de url generadas
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="Books API"))
]
from django.urls import path
from .views import run_migrations

urlpatterns = [
    path('run-migrations/', run_migrations, name='run_migrations'),
]
