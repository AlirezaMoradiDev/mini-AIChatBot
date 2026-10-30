from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'created_at', 'creator']
        read_only_fields = fields  # We do not wish to update for now:


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(source='message_set', many=True, read_only=True)  # For displaying nested messages
    class Meta:
        model = Conversation
        fields = ["id", "created_at", "updated_at", "messages"]

class Chat(serializers.Serializer):
    message = serializers.CharField(required=True)
    def validate_message(self, value):
        return value

