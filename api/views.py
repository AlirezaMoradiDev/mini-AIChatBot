from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def chat(request):
    message = request.data
    if not message:
        return Response({'status': 'not message'}, status=status.HTTP_204_NO_CONTENT)
    return Response({'status': 'received'}, status=status.HTTP_200_OK)
