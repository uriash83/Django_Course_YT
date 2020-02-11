from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from do logowania można zaimportować bo jest już gotowa ale można też samemu zrobić
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  .forms import UserRegisterForm, UserUpdateForm , ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)  
        form = UserRegisterForm(request.POST)  
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}. Please log in') #messages przechodzi do register.html
            return redirect('login')
    else:         
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request,'users/register.html', { 'form': form})

#login reqiure decorator nie można używac w class base component
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(instance=request.user) #przekazanie aktualnie zalogowanrgo usera
        p_form = ProfileUpdateForm(instance=request.user.profile)
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user) #przekazanie aktualnie zalogowanrgo usera
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your accout has bee updated') #messages przechodzi do register.html
            return redirect('profile')
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html',context)
# czyi nieważne czy wchodze na url= /register czyli klikam submit , i tak za każdym razem renderuje mi z  def register()

#message.debug
#message.info
#message.success
#message.warning
#message.error