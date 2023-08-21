from rest_framework import serializers 
from api.models import Company,Employee

#Creat serializers Here.
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields='__all__'
#Create EmployeeSerializers Here
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        modele = Employee
        fields = '__all__'