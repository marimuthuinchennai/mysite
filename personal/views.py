from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
def index(request):
    return render(request,"base.html")

def page1(request):
    empdet=Employee.objects.all()
    return render(request,'page1.html',{'emp':empdet})
def page2(request):
    form = PostForm()
    return render(request,'page2.html',{'form': form})
def post_new(request):
    empdet=Employee.objects.all()
    form = PostForm()
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email = request.POST.get('email')
    phonenumber=request.POST.get('phonenumber')
    Employee(first_name=first_name,last_name=last_name,mail=email,phonenumber=phonenumber).save()
    return render(request,'page2.html')
    #HttpResponseRedirect('/page1/')
    #if request.method == "POST":

    #    form = PostForm(request.POST)
    #    if form.is_valid():
            #post = form.save(commit=False)
            #post.save()
    #        form.save()
            #return render(request,'page1.html',{'emp':empdet})
    #else:
    #    form = PostForm()
    #return render(request, 'blog/post_edit.html', {'form': form})
