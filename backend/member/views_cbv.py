from django.shortcuts import render
from django.shortcuts import render
from django.urls import path
from . import views_cbv
# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from member.models import MemberVO
from member.serializers import MemberSerializer
from icecream import ic


class Members(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        ic(serializer.errors)
        return Response(serializer.errors, status=400)


class Member(APIView):
    def post(self, request):
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = self.get_object(pk)
        if user_input_password == member.password:
            return Response({'result': 'you are logged in'}, status=201)
        return HttpResponse(status=104)#이거 뭐징???
        # print(type(member)): when pk is correct, <class 'member.models.MemberVO'>
        # print(member.pk) = print(member.username)