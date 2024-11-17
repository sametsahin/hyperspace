from django.http import HttpResponse

def test(request):
    return HttpResponse("It is a test page")