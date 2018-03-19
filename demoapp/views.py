from django.shortcuts import render, render_to_response
from django.template import RequestContext
from models import UserStory, AcceptanceCriteria


def index(request):
    if request.method == 'USERSTORY':
        # US_IDs = request.USERSTORY['US_IDs']

        US_Name = request.USERSTORY['US_Name']
        US_As = request.USERSTORY['US_As']
        US_IWant = request.USERSTORY['US_IWant']
        US_SoThat = request.USERSTORY['US_SoThat']
        US_Priority = request.USERSTORY['US_Priority']

        # AC_Name = request.USERSTORY['AC_Name']
        # AC_Given = request.USERSTORY['AC_Given']
        # AC_When = request.USERSTORY['AC_When']
        # AC_Then = request.USERSTORY['AC_Then']
        # AC_Negative = request.USERSTORY['AC_Negative']

        userstory = UserStory(US_ID=US_ID, US_Name=US_Name, US_As=US_As, US_IWant=US_IWant, US_SoThat=US_SoThat, US_Priority=US_Priority)
        # userstory.US_Name = US_Name
        # userstory.US_As = US_As
        # userstory.US_IWant = US_IWant
        # userstory.US_SoThat = US_SoThat
        # userstory.US_Priority = US_Priority

        userstory.save()

    userstories = UserStory.objects
    return render_to_response(
        'index.html', {'UserStories': userstories},
        context_instance=RequestContext(request))

def update(request):
    id = eval("request." + request.method + "[id]")
    userstory = UserStory.objects(id=id)[0]
    if request.method == 'USERSTORY' 
        userstory.US_Name = request.USERSTORY['US_Name']
        userstory.US_As = request.USERSTORY['US_As']
        userstory.US_IWant = request.USERSTORY['US_IWant']
        userstory.US_SoThat = request.USERSTORY['US_SoThat']
        userstory.US_Priority = request.USERSTORY['US_Priority']
        userstory.save()
        template = 'index.html'
        params = {'UserStories': UserStory.objects}
    
    elif: request.method=='GET':
        template = 'update.html'
        params = {'userstory': userstory}
    
    return render_to_response(template, params, context_instance=RequestContext(request))
