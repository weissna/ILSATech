from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html="""  <div class=\"container\">    <label><b>Username</b></label>
    <input type=\"text\" placeholder=\"Enter Username\" name=\"uname\" required>
    <br>
    <label><b>Password</b></label>
    <input type=\"password\" placeholder=\"Enter Password\" name=\"psw\" required>
    <br>
    <button type=\"submit\">Login</button>
  </div>"""
    return HttpResponse(html)