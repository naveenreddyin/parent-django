from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def generate_token(request):
    """
    :param request:
    :return:
    """

    data = {
        "message":1232
    }
    if request.method == 'GET':
        return Response(data)
