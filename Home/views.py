from django.shortcuts import render
# from .models import Program

# Create your views here.
def home(request):
   # programkita = Program.objects.all()
   # return render(request, 'index.html', {'programs': programkita})
   return render(request, 'home.html', {})

