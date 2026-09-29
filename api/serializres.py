from rest_framework import serializers



class Chat(serializers.Serializer):
    message = serializers.CharField(required=True)
    def validate_message(self, value):
        return value

