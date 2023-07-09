from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
# Create your views here.

class HomeView(View):
    
    template_name = "index.html"
    contexto = {"home": True}

    def get(self, request):
        return render(request,self.template_name,self.contexto)