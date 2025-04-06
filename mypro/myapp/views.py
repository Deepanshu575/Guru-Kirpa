from django.shortcuts import render # type: ignore


# Create your views here.
def get_name(request):
    name=""
    if request.method=="POST":
        name=request.POST.get("name")
    return render(request,'index.html',{"name":name}) 
