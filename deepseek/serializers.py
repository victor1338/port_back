from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    role = serializers.CharField()
    content = serializers.CharField()

class ChatCompletionRequestSerializer(serializers.Serializer):
    messages = MessageSerializer(many=True)
    model = serializers.CharField(default="deepseek-chat")
    temperature = serializers.FloatField(default=0.7, required=False)
    max_tokens = serializers.IntegerField(default=None, required=False, allow_null=True)

class ChatCompletionResponseSerializer(serializers.Serializer):
    message = MessageSerializer()
    usage = serializers.DictField() 