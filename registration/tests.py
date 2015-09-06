from django.test import TestCase
from .models import User, UserProfile, GoogleRegistrationId, ConnectModel

# Create your tests here.
class RegistrationTest(TestCase):
    regidp = "dsdgdsg33344354"
    regidc1 = "sdfsdg3223sdgdsgdg"
    regidc2 = "sdfsdgdskgdog3243253453453453436336"

    phonenop = "34235235"
    phonenoc1 = "2342432432"
    phonenoc2 = "823235235"

    typep = 1
    typec = 0

    def setUp(self):
        regidp = GoogleRegistrationId.objects.create(registration_id=self.regidp)
        userprofilep = UserProfile.objects.create(regid=regidp, type=self.typep)
        userp = User.objects.create(phone_no=self.phonenop, user_profile=userprofilep)

    def test_1(self):
        userp = User.objects.all()
        for auser in userp:
            print auser.user_profile.type
