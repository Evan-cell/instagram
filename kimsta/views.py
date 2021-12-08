from email import message
from django.shortcuts import redirect, render
from .models import posts #import photos model

def insta(request):
    # imports photos and save it in database
    photo = posts.objects.all()
    # adding context 
    ctx = {'photo':photo}
    return render(request, 'temps/insta.html', ctx)
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            message.success(request, 'Account was created for ' + user)
			
            return redirect('login/')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)    