from models import Patient
from rest_framework.serializers import ModelSerializer

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'phonenumber', 'password')
    
    # def __init__(self, *args, **kwargs):
    #     super(ModelSerializer, self).__init__(*args, **kwargs)

