from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "about.html")


def education(request):
    return render(request, "educational.html")

def contact(request):
    if request.method == 'POST':
       formData = request.POST
       sent_name = formData.get('name')
       sent_email = formData.get('email')
       sent_message = formData.get('message')

       message_sent = True
       context= {
        "message_sent" : message_sent
    }       
       
       return render(request, "contact.html", context)

       
    return render(request, "contact.html")


def home(request):


    return render(request, "home.html")