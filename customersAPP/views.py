from django.shortcuts import render
import json
from django.views import View
from .models import Costumer
from django.http import JsonResponse, HttpResponseRedirect
from django.forms import model_to_dict
from .serializers import CostumerSerializer
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
#Django Rest Framework
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,action


# Create your views here.

# Class view for costumer list
class CostumerView(viewsets.ModelViewSet):
    queryset = Costumer.objects.all()
    serializer_class = CostumerSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self,request):
        serializer = CostumerSerializer(data = request.data)
        if serializer.is_valid():
            costumer = serializer.save(lastupdateuser=self.request.user,creatoruser=self.request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Costumer.objects.all()
        serializer = CostumerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Costumer.objects.all()
        costumer = get_object_or_404(queryset, pk=pk)
        serializer = CostumerSerializer(costumer)
        return Response(serializer.data)

    def create(self, request):
        serializer = CostumerSerializer(data = request.data)
        if serializer.is_valid():
            costumer = serializer.save(lastupdateuser=self.request.user,creatoruser=self.request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        queryset = Costumer.objects.all()
        costumer = get_object_or_404(queryset, pk=pk)
        serializer = CostumerSerializer(costumer, data=request.data)
        if serializer.is_valid():
            serializer.save(lastupdateuser=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def destroy(self, request, pk=None):
        queryset = Costumer.objects.all()
        costumer = get_object_or_404(queryset, pk=pk)
        costumer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
    
#Class to login the user
class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('costumer_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

#class for logout
class Logout(APIView):
    def get(self,request,format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)