from rest_framework import viewsets
from .serializer import BooksSerializer
from .models import Books

# Clase para proporsionar operaciones CRUD para este modelo
class BooksView(viewsets.ModelViewSet):
    
    queryset = Books.objects.all()#Consulta a la BD
    serializer_class = BooksSerializer 

def check_books_data(request):
    books = list(Book.objects.values())  # Convierte los registros en un diccionario
    return JsonResponse({"books": books})
