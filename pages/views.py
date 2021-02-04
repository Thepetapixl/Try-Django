from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>") #string of html code
    return render(request, "home.html", {})

def contact_views(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Us</h1>") 

def aboutus(request, *args, **kwargs):
    my_context ={
        "my_text" : "this is about us and not about me",
        "this_is_true" : True,
        "my_number" : 9881233445,
        "my_list" : [1,2,3,4,"xyz"],
        "my_html" : "<h3>This is the html tag i was talking about</h3>"
    }
    return render(request, "about.html", my_context)