from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializres import Chat
from .business_logic import ChatLogic


@api_view(['POST'])
def chat(request):
    serializer = Chat(data=request.data)
    if serializer.is_valid():
        message = serializer.validated_data.get('message')
        chat = ChatLogic(message)
        return Response({'answer': chat.answer(), 'msg': message}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
