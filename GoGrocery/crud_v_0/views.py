from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.

def inicio_view(request,*args, **kwargs):
    print(request,args,kwargs)
    return render(request,"base.html",{})



# vista login usuarios -------------------------------------------------
from .forms import loggin_form
def loggin_view(request):
    loginform = loggin_form(request.POST)

    if request . method == 'POST' :

        #Verfificacion de usuariotss
        pass
        # import bcrypt
        # '$2b$12$shXHudKu20Vs/d8sFjp3ueI4pOa2rc2Q.ACwF7Fk1i2ycpEYXUCHG' = 123
        # bcrypt.checkpw(b'password',b'hash') = True or False
        #request.POST['email']
        #request.POST['pass'] 

    contexto = {
        'form':loginform
    }
    return render(request,'loggin.html',contexto)   
#-----------------------------------------------------------------------


#--Vista Olvido de contraseña-------------------------------------------
def forgot_view(request):
    return render(request,"forgot.html",{})
#-----------------------------------------------------------------------