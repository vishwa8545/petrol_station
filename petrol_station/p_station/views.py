from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from . forms import RegistrationForm
from . models import Stations,UserProfileMode
from django.views.generic import CreateView


# Create your views here.
class Register(CreateView):
    form_class = RegistrationForm
    template_name = "register.html"


    def dispatch(self,request,*args,**kwargs):
    	return super(Register,self).dispatch(request,*args,**kwargs)

    
    def form_valid(self,form):
    	user = form.save(commit=False)
    	user.set_password(form.cleaned_data['password'])
    	user.save()
    	UserProfileMode.objects.create(user=user)
    	return render(request,'login.html')
def station(request):
	fs = Stations.objects.all()
	context = {'stations':fs}

	return render(request,'home.html',context)

def update(request):
	if request.method == "POST":
		op_type = request.POST['op_type']
		if op_type == 'add':
			stt_id = request.POST['st_id'] 
			f_value = int(request.POST['f_value'])
			fu_level = int(request.POST['sf_value'])+f_value
			station = Stations.objects.get(pk=stt_id)
			station.fueil_level =  fu_level
			station.station_type = request.POST['st_name']
			station.pk = stt_id

			station.save()
			station = Stations.objects.all()
			context ={
			'stations':station
			}

			return render(request,'home.html',context)
		
		
		elif op_type == 'sold':
			stt_id = request.POST['st_id'] 
			f_value = int(request.POST['f_value'])
			fu_level = int(request.POST['sf_value'])-f_value
			station = Stations.objects.get(pk=stt_id)
			station.fueil_level =  fu_level
			station.station_type = request.POST['st_name']
			station.pk = stt_id

			station.save()
			station = Stations.objects.all()
			context ={
			'stations':station
			}

			return render(request,'home.html',context)


def login_view(request):
	if request.method=="POST":
		form  = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			station = Stations.objects.all()
			return render(request,'home.html',{'stations':station})


	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})
def index(request):
	return render(request,'index.html')