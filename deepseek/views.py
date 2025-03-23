from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatCompletionRequestSerializer, ChatCompletionResponseSerializer
from .client import DeepseekClient
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ChatCompletionView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatCompletionRequestSerializer(data=request.data)
        if serializer.is_valid():
            client = DeepseekClient()
            try:
                response = client.chat_completion(**serializer.validated_data)
                
                response_data = {
                    'message': {
                        'role': response.choices[0].message.role,
                        'content': response.choices[0].message.content,
                    },
                    'usage': response.usage.model_dump()
                }
                
                response_serializer = ChatCompletionResponseSerializer(data=response_data)
                if response_serializer.is_valid():
                    return Response(response_serializer.data)
                return Response(response_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
