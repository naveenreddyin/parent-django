from django.shortcuts import render, render_to_response
from django.template import RequestContext
from push_notifications import *

# Create your views here.
def send_push(request):
    """
    Business User registration view.
    """

    return render_to_response('gcm/register.html', context_instance=RequestContext(request))
