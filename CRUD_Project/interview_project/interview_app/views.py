from django.shortcuts import render,redirect
from django.views import View
from .models import InterviewSession 
from .forms import AddUserForm
# Create your views here.

class Home(View):
    def get(self, request):
        interview_data = InterviewSession.objects.all() #fetching all data inside the data
        return render(request,'src/index.html',{'interview_data':interview_data})

#method to add student
class Add_User(View):
    def get(self,request):
        forms = AddUserForm()
        return render(request,'src/add_user.html',{'form':forms})
    def post(self,request):
        forms = AddUserForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/')
        else:
            return render(request,'src/add_user.html',{'form':forms})

class DeleteUser(View):
    def post(self,request):
        data = request.POST
        first_name = data.get('id')
        # use try catch to delete alawys 
        i_data = (InterviewSession.objects.get(first_name=first_name))
        i_data.delete()
        return redirect('/')