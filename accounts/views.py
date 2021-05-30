# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# # Create your views here.
# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)#this instance of the form has the user's data which he input
#         if form.is_valid(): #checks for validity
#             form.save()  #saves at the database
#             #log the user in
#             return redirect('articles:list') #redirect to articles list page
#     else: #if it is not a post request, then the else part is executed which has  blank instance of the form
#           #this scenario happens when the user directly tries to go to the /signup page via the address bar
#      form = UserCreationForm() #this is a blank instance of the form
#      return render(request,'accounts/signup.html',{'form':form}) 

#      #there is a third scenario, where the request is post, but the form is not valid, even then, the post 
#      #instance of the form is created and hence, it jumps out of the if statement in the 7th line and comes 
#      #directly to the 14th line, here the form with the user's data is again sent back(to the same page)

  
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)        
             return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            user = form.get_user()   #retreive the user
            login(request, user)           # login the user using login function
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) #gets the value from the login.html file where we had speicifed the name of the input field to be 'next'
            else:
                return redirect('articles:list')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')