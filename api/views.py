from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializres import MessageSerializer, ConversationSerializer
from .business_logic import ChatLogic
from .models import Conversation, Message



@api_view(['GET'])
def list_conversation(request):
    conversations = Conversation.objects.all()
    serializer = ConversationSerializer(conversations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_conversation(request, id):
    try:
        conversation = Conversation.objects.get(id=id)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Conversation.DoesNotExist:
        return Response('conversation not exist', status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# def chat(request):
#     serializer = Chat(data=request.data)
#     if serializer.is_valid():
#         message = serializer.validated_data.get('message')
#         chat = ChatLogic(message)
#         return Response({'answer': chat.answer(), 'msg': message}, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
