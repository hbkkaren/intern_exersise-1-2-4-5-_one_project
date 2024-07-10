from django.shortcuts import render,redirect
from .models import *




def index(request):
    return render(request,'new.html')



def register(request):
    if request.method == "POST":
        

        try:

            User.objects.get(email = request.POST['email'])
            msg = 'User is alrady registered'
            content = User.objects.all().reverse

            return render(request,'home.html',{'msg':msg,'content':content})
        
        except:

            User.objects.create(
                username = request.POST['username'],
                email = request.POST['email'],
            )
            msg = 'register sucessfully'

            content = User.objects.all().reverse
            return render(request,'home.html',{'msg':msg,'content':content})
        
    else:
     content = User.objects.all()


     return render(request,'home.html',{'content':content})
    



def remove(request,pk):
    
    User.objects.get(pk=pk).delete()

    msg = 'data deleted '

    return redirect('resister')



def add_quotes(request):

    if request.method == "POST":

        msg = ' return render(request,"add-quotes.html")'
        try:
            User.objects.get(email=request.POST['email'])

            Quotes.objects.create(

                author_name = request.POST['author_name'],
                quotes = request.POST['quote'],
            )

            msg = 'quote added successfully'

            return render(request,"add-quotes.html",{'msg':msg})
        
        except User.DoesNotExist:
            msg = 'first register as user'

            return render(request,"add-quotes.html",{'msg':msg})





    else:
        return render(request,"add-quotes.html")
    

def all_quotes(request):
    data = Quotes.objects.all()
    context = {'data':data}
    return render(request,'all_quotes.html',context)



def remove_quote(request,pk):
    
    Quotes.objects.get(pk=pk).delete()

    msg = 'data deleted '

    return redirect('all_quotes')

    


    





    
