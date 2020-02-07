from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from do logowania można zaimportować bo jest już gotowa ale można też samemu zrobić
from django.contrib import messages
from  .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)  
        form = UserRegisterForm(request.POST)  
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}') #messages przechodzi do register.html
            return redirect('blog-home')
    else:         
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request,'users/register.html', { 'form': form})
# czyi nieważne czy wchodze na url= /register czyli klikam submit , i tak za każdym razem renderuje mi z  def register()

#message.debug
#message.info
#message.success
#message.warning
#message.error