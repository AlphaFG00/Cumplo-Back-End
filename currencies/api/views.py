from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import CurrencieSerializer
import requests,json



class CurrenciesListAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = CurrencieSerializer(data=request.data)
        try:
            if serializer.is_valid():
                currency = serializer.data['currency']
                banxico_data = self.get_banxico_data(serializer.data, currency)
                return Response(data=self.get_depurated_data(banxico_data, currency), status=200)
            else:
                return Response(data=serializer.errors, status=400)
        except Exception as e:
            return Response(data=e.args[0], status=400)

    def get_banxico_data(self, data, currency):
        init_date = data['init_date']
        end_date = data['end_date']
        headers = {'Bmx-Token': settings.BANXICO_TOKEN }
        url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{currency}/datos/{init_date}/{end_date}"
        response = requests.get(url=url, headers=headers).json()
        return response

    def get_depurated_data(self, data, currency):
        if currency in ["SP68257", "SF43718"]:
            depured = data['bmx']['series'][0]['datos']
            values = []
            for i in depured:
                values.append(float(i['dato']))
            total = sum(values) / len(depured)
            currency_min = min(values)
            currency_max = max(values)
            return {"average": total ,"min": currency_min, "max": currency_max, "currency_values": depured}
        else:
            TIIE_1 = data['bmx']['series'][0]['datos']
            TIIE_2 = data['bmx']['series'][1]['datos']
            TIIE_3 = data['bmx']['series'][2]['datos']
            TIIE_4 = data['bmx']['series'][3]['datos']
            return {"T1": TIIE_1, "T2": TIIE_2, "T3":TIIE_3, "T4":TIIE_4}



