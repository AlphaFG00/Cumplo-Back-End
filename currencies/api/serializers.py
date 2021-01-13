from rest_framework import serializers


class CurrencieSerializer(serializers.Serializer):
    init_date = serializers.DateField(format="%Y-%m-%d", required=True)
    end_date = serializers.DateField(format="%Y-%m-%d", required=True)
    currency = serializers.CharField(required=True)

    





