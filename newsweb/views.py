from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    apireq=requests.get("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=880e5ce759e74f599325bbb4e3dcafa0")
    api=json.loads(apireq.content)
    return render(request,'news.html',{'api':api})