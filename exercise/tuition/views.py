from django.shortcuts import render,redirect
from .models import contact,post

from .forms import contactmodForm
# Create your views here.g hjg

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'base.html', {})

def contract(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        obj = contact(name=name,message=message,subject=subject) 
        obj.save()

         #object create krbo jekhane model er field gulu rakhbo and save krbo
         # 1st name => model field name and 2nd name => view field name 

    # ______________________________ GET_______________________________________

# if request.method=="GET":
#     #     name=request.GET.get('name')
#     #     email=request.GET.get('email')
#     #     subject=request.GET.get('subject')
#     #     message=request.GET.get('message')
#     #     print(name)
#     #     print(email)
#     #     print(subject)
#     #     print(message)
     
       
        
    return render(request, 'contract.html', {})
    
    


    # ______________________________ Form_______________________________________

    
# def contactForm(request):
#     if request.method=="POST":
#         form=contactForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             message=form.cleaned_data['message']
#             subject=form.cleaned_data['subject']

#             print(name)
#             print(message)
#             print(subject)
#             obj = contact(name=name,message=message,subject=subject) 
#             obj.save()        

#     else:
#         form=contactForm() 

#     return render(request, 'contractForm.html', {'form' : form})
        
    

    # ______________________________ ModelForm_______________________________________
    
def contactmodelForm(request):
    show_data=contact.objects.all()
 
    
    if request.method=="POST":
        form=contactmodForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # message=form.cleaned_data['message']
            # subject=form.cleaned_data['subject']

            # print(name)
            # print(message)
            # print(subject)
            # obj = contact(name=name,message=message,subject=subject) 
            # obj.save()      
            form.save()  

    else:
        form=contactmodForm() 

    context={
        'form' : form,
        'show_data': show_data 
    }    

    return render(request, 'contractForm.html', context)


def postview(request):
    posts = post.objects.all()
    context={
        'posts':posts
    }
    return render(request,'postview.html',context)


