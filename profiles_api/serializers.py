from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializes name field for testing APIviews"""
    name = serializers.CharField(max_length = 10)
