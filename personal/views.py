from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.edit import FormView
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.shortcuts import get_list_or_404, get_object_or_404

class EmpUpdateView(UpdateView):
    model = Employee
    form_class = PostForm
    #fields = ['first_name']
    template_name = 'personal/employee_update_form.html'
    #queryset=Employee.objects.all()
    success_url = '/page1/'
    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Employee,id=id_)
class ContactView(FormView):
    template_name = 'personal/create.html'
    form_class = PostForm
    success_url = '/page1/'
    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        mail = form.cleaned_data['mail']
        phonenumber = form.cleaned_data['phonenumber']
        Employee(first_name=first_name,last_name=last_name,mail=mail,phonenumber=phonenumber).save()
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        #return super().form_valid(form)
        return super(ContactView, self).form_valid(form)
class ArticleListView(ListView):
    model = Employee
    #paginate_by = 100  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

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
