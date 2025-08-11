from rest_framework import serializers


class GenerateSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    tipo = serializers.ChoiceField(choices=["model", "view", "serializer", "template"])
