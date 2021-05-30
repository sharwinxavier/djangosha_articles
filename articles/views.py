from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles=Article.objects.all().order_by('date')
    #here in the above line, the variable 'articles' stores all the instances of the class Article inside it in a date-sorted order-->
    return render(request,'articles/article_list.html', {'articles': articles})
    #here in the above line, the third parameter, is defined as a dictionary which has the value 'articles' defined in the 6th line"-->

def article_details(request,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_details.html',{'article': article})

@login_required(login_url="/accounts/login/")  #decorator which checks whether login is required for a page
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES) # the second parameter is used, as we are uploading files too
        if form.is_valid():
            instance = form.save(commit=False)  #this third parameter waits for a short time before saving, thus I've stored it in a variable called 'instance'
            instance.author = request.user # we have access to the user when there is a post request, we grab that user and store it in the author field of the instance variable which stores the form data
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form': form})