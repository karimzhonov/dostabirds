from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request):
        return Response({'method': 'get', 'text': 'test'})

    def post(self, request):
        return Response({'method': 'post', 'data': request.body})


