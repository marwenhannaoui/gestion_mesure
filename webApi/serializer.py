from rest_framework import serializers
from grandeurs.models import Grandeur

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grandeur
        fields=('nom','unite','valeurMin','valeurMax')