from django.shortcuts import render_to_response

def home(request) :
    content = "<h3>Lorem Ipsum</h3><p>Lorem ipsum dolor sit amet</p>"
    return render_to_response("home.html", locals())
