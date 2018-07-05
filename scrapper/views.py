from django.http import StreamingHttpResponse
from .selenium import scrap


def start(request):
    return StreamingHttpResponse(scrap())
