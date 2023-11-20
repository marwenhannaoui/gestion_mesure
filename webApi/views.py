
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DataSerializer
from grandeurs.models import Grandeur
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def getData(request):
    app = Grandeur.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(Grandeur, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['PUT'])
def update_items(request, pk):
	item = Grandeur.objects.get(pk=pk)
	data = DataSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
