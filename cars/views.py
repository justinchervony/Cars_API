from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Car

@api_view(['GET'])
def cars_list(request):

    return Response('ok')
