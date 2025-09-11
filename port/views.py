from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def education(request):
    return render(request, "education.html")

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


def about(request):


    return render(request, "about.html")