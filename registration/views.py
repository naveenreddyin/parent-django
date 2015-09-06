from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from registration.models import User, GoogleRegistrationId, UserProfile, ConnectModel


@api_view(['POST'])
def register_parent_app(request, phone_no):
    data = {}
    response = 0
    if request.method == 'POST':
        try:
            registration_id = request.data["gid"]
            print str(registration_id[0])
            profile_type = request.data["type"]
            print profile_type[0]
            google_registration_id = GoogleRegistrationId.objects.create(registration_id=registration_id[0])
            user_profile = UserProfile.objects.create(regid=google_registration_id, type=profile_type[0])
            r = User(phone_no=phone_no, user_profile=user_profile)
            r.save()
            response = 1
            message = "Saved to database"
        except Exception as e:
            print e
            response = 0
            message = e.message
        data.update({
            'response': response,
            'message': message
        })
        return Response(data)


@api_view(['POST'])
def connect_app_register(request, child_no, parent_no):
    data = {}
    try:
        registration_id = request.data["gid"]
        print str(registration_id[0])
        profile_type = request.data["type"]
        print profile_type[0]
        google_registration_id = GoogleRegistrationId.objects.create(registration_id=registration_id[0])
        user_profile = UserProfile.objects.create(regid=google_registration_id, type=profile_type[0])
        child = User.objects.create(phone_no=child_no, user_profile=user_profile)

        parent = User.objects.get(phone_no=parent_no)

        ConnectModel.objects.create(parent_device=parent, child_device=child)
        response = 1
        message = "Saved to database"
    except Exception as exception:
        print exception
        response = 0
        message = exception.message

    data.update({
        'response': response,
        'message' : message
    })

    return Response(data)