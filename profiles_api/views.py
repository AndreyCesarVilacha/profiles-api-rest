from rest_framework.views import APIView
#Responsavel por gerênciar as respostas do APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        #most be a list or dictionary to convert to json
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
