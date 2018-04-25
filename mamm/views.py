# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#Default
import requests
import openpyxl

#Django
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

#Rest_Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

#Own
from models import Patient, Stuff, MedicalHistory, MedicalHistoryExcel, MedicalHistoryExcelTemplate, PatientOnlyPhone
from serializers import PatientSerializer



# Create your views here.

class PatientViewSet(ModelViewSet):
    # this fetches all the rows of data in the Patient table
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

def index(request):
    templates = MedicalHistoryExcelTemplate.objects.all()
    context = {
        'templates': templates
    }
    for template in templates:
        print(template.excel.path)
    print(templates)
    return render(request, 'mamm/medical/index.html', context)

"""
SMS Service
"""

def send_sms_to_stuff(patient):
    stuffs = Stuff.objects.all()
    send_string = "Name:" + patient.first_name +\
                 "\nPhone:" + patient.phonenumber

    print(send_string)
    for stuff in stuffs:

        payload = {
            'userid' : "",
            'account' : "jkwl518",
            'password' : "jkwl51825",
            'mobile' : stuff.phone,
            'content': "Patient Ordered Service!\nUser Detail\n" +send_string+ "【爱克】",
            'sendTime' : "",
            'extno' : ""
        }

        headers = {'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

        r = requests.post("https://sh2.ipyy.com/smsJson.aspx?action=send", data=payload, headers=headers)
        print(r.status_code)

def send_verify_sms(phonenumber, verifycode):
    payload = {
        'userid' : "",
        'account' : "jkwl518",
        'password' : "jkwl51825",
        'mobile' : verifycode,
        'content': "Verify Code is "+ phonenumber +"【爱克】",
        'sendTime' : "",
        'extno' : ""
    }

    headers = {'content-type': 'application/x-www-form-urlencoded;charset=utf-8'}

    r = requests.post("https://sh2.ipyy.com/smsJson.aspx?action=send", data=payload, headers=headers)
    return r.status_code

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']
        
        try:
            patient = Patient.objects.get(email=email)
        except Patient.DoesNotExist:
            patient = None
        if patient is not None:

            if check_password(password, patient.password):
                send_data = {
                    'first_name': patient.first_name,
                    'last_name': patient.last_name,
                    'email': patient.email,
                    'phonenumber': patient.phonenumber,
                    'chujonservice': patient.chujonservice,
                    'huijonservice': patient.huijonservice,
                    'jiuyiservice': patient.jiuyiservice

                }
                return Response({'user': send_data , 'token':patient.email }, status=status.HTTP_201_CREATED)

            else:
                return Response({'error':{'message':"Password Incorrect!"}})
        else:
            return Response({'error':{'message':"User doesn't exist"}})


@api_view(['POST'])
def register(request):
    print("Register")
    if request.method == 'POST':
        email = request.data['email']
        print(email)
        try:
            patient = Patient.objects.get(email=email)
        except Patient.DoesNotExist:
            patient = None

        if patient is None:
            password = request.data['password']
            print(make_password(password))
            request.data['password'] = make_password(password)
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': { 'message':"User with that email already exist!"}})


@api_view(['POST'])
def chuzonservice(request):
    if request.method == 'POST':
        email = request.data['email']

        try:
            patient = Patient.objects.get(email=email)
        except Patient.DoesNotExist:
            patient = None

        if patient is not None:
            # send_sms_to_stuff(patient)
            return Response({},status = 200)

        else:
            return Response({'error': {'message':"Can't find user"}}, status=400)

    return Response({'error': { 'message' : "Failed"}}, status=400)


@api_view(['GET'])
def getmedicalhistory(request):
    print ("getmedical")

    if request.method == 'GET':
        historys = MedicalHistoryExcel.objects.all()
        send_data = []

        for history in historys:
            print(history.excel)
            book = openpyxl.load_workbook(history.excel)
            sheet = book.active
            dicti = {}

            dicti['patient_name'] = history.patient.first_name + ' ' + history.patient.last_name
            dicti['creation_date'] = history.creation_date

            excel_data = []
            for rowObjects in sheet[sheet.dimensions]:
                if rowObjects[1].value is not None:
                    excel_dictionary = {}
                    excel_dictionary[rowObjects[0].value] = rowObjects[1].value
                    excel_data.append(excel_dictionary)

            dicti['excel_data'] = excel_data
    
            if history.image1:
                print(history.image1.url)
                dicti['image1'] = history.image1.url

            if history.image2:
                dicti['image2'] = history.image2.url

            if history.video1:
                dicti['video1'] = history.video1.url
            send_data.append(dicti)

        return Response({'data': send_data },status = 200)

@api_view(['POST'])
def forgotpass(request):
    try:
        email = request.data['email']
    except KeyError:
        return Response({'error':{'message':'KeyError'}})

    try:
        patient = Patient.objects.get(email=email)
    except Patient.DoesNotExist:
        patient = None

    if patient is not None:
        rand_str = get_random_string(length=6, allowed_chars='1234567890')
        patient.verifycode = rand_str
        patient.save()
        if patient.phonenumber is not None:
            statuscode = send_verify_sms(patient.phonenumber, rand_str)
            return Response({'data': 'Success'}, status=200)
        else:
            return Response({'error' : {'message':'Patient phone number does not exist'}})

    return Response({'error' : {'message':'Patient does not exist'}})

@api_view(['POST'])
def verifycode(request):
    email = request.data['email']
    verifycode = request.data['verifycode']

    try:
        patient = Patient.objects.get(email=email)
    except Patient.DoesNotExist:
        patient = None

    if patient is not None:
        if patient.verifycode == verifycode:
            return Response({'data':'Success'}, status=200)
        else:
            return Response({'error':{'message':'Wrong Verify Code'}})

    return Response({'error': {'message' : 'Failed'}})

@api_view(['POST'])
def setpass(request):
    email = request.data['email']
    password = request.data['password']

    try:
        patient = Patient.objects.get(email=email)
    except Patient.DoesNotExist:
        patient = None

    if patient is not None:
        patient.password = make_password(password)
        patient.save()
        return Response({'data':'Success'}, status= 200)

    return Response({'error': { 'message': 'Failed'}})


"""
Login with Phone
"""
@api_view(['POST'])
def loginphone(request):
    try:
        phone = request.data['phone']
    except KeyError:
        return Response({'error':{'message':'KeyError'}})
    
    try:
        patient = PatientOnlyPhone.objects.get(phonenumber=phone)
    except PatientOnlyPhone.DoesNotExist:
        patient = None
    
    if patient is None:
        patient = PatientOnlyPhone.objects.create(phonenumber=phone)
    
    rand_str = get_random_string(length=6, allowed_chars='1234567890')
    print(rand_str)
    patient.verifycode = rand_str
    patient.save()
    status_code = send_verify_sms(patient.phonenumber, rand_str)

    if status_code == 200:
        send_data = {
            'phonenumber': patient.phonenumber,
            'chujonservice': patient.chujonservice,
            'huijonservice': patient.huijonservice,
            'jiuyiservice': patient.jiuyiservice

        }
        return Response({ 'user': send_data, 'token': patient.phonenumber }, status=200)
    else:
        return Response({'error': {'message': 'Failed'}}, status=status_code)

@api_view(['POST'])
def verifycode_phone(request):
    phone = request.data['phone']
    verifycode = request.data['verifycode']

    try:
        patient = PatientOnlyPhone.objects.get(phonenumber=phone)
    except Patient.DoesNotExist:
        patient = None

    if patient is not None:
        if patient.verifycode == verifycode:
            return Response({'data':'Success'}, status=200)
        else:
            return Response({'error':{'message':'Wrong Verify Code'}})

    return Response({'error': {'message' : 'Failed'}})
