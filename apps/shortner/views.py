from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import NanoLink
from .serailizers import NanoLinkSerailzer


class NanoLinkViewSet(viewsets.ModelViewSet):
    queryset = NanoLink.objects.all()
    serializer_class = NanoLinkSerailzer
    
    def create(self, request):
        serializer = NanoLinkSerailzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            nano_link = NanoLink.objects.get(pk=pk)
        except NanoLink.DoesNotExist:
            return Response({'error': 'Link not found'}, status=status.HTTP_404_NOT_FOUND)
        nano_link.acces_count += 1
        nano_link.save()
        serialzer = NanoLinkSerailzer(nano_link)
        return Response(serialzer.data, status=status.HTTP_200_OK)
