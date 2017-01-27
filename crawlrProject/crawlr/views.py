from django.shortcuts import render
from django.http import HttpResponseRedirect
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from calculate import start_chain

def application(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        data = request.POST
        start_chain(data)
        return render(request, 'application-test.html')

            #redirect to results page?


    return render(request, 'application-full.html')

# def application(request):
#     page = render(request, 'application.html')
#     return page