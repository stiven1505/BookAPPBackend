from rest_framework import viewsets
from .serializer import BooksSerializer
from .models import Books

# Clase para proporsionar operaciones CRUD para este modelo
class BooksView(viewsets.ModelViewSet):
    
    queryset = Books.objects.all()#Consulta a la BD
    serializer_class = BooksSerializer 
# En tu archivo views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.management import call_command

@csrf_exempt  # Deshabilitar CSRF para esta vista (solo para propósitos de desarrollo)
def run_migrations(request):
    if request.method == 'POST':
        try:
            call_command('migrate')
            return JsonResponse({'message': 'Migraciones ejecutadas con éxito.'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Método no permitido.'}, status=405)
