from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over  you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message':'HELLO~','an_apiview': an_apiview})
