from rest_framework import serializers
from .models import Books

#clase para convertir los datos a JSON
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        #fields = ('id', 'name') Forma de hacerlo por columnas
        fields = '__all__'