from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView , CreateAPIView
from .models import Link
from .serailizers import LinkSerializer
from django.views import View
from django.conf import settings
# Create your views here.

class ShortnerListAPIView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    
class ShortnerCreateAPIView(CreateAPIView):
    serializer_class = LinkSerializer
    
class Redirector(View):
    def get(self,request,nano_link,*args,**kwargs):
        shortner_link = settings.HOST_URL+'/'+self.kwargs['nano_link']
        redirect_link = Link.objects.filter(nano_link=shortner_link).first().original_link
        return redirect(redirect_link)    