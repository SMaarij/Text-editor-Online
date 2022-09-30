# We created this file
from django.http import HttpResponse
from django.shortcuts import render


                                #For video 6
# def index(request):
#     return HttpResponse("<h1>Hello</h1>")
#
# def about(request):
#     return HttpResponse("Hello by about page")

                                #Laying the pipeline
def index(request):
    # params = {'name':'harry','age':32}
    return render(request,'index.html')#params

                
                #Laying the pipeline
    # return HttpResponse('''Home <br><button><a href=http://127.0.0.1:8000/removepunc>Go to remove punc </button></a>
    # <br><button><a href=http://127.0.0.1:8000/capfirst>Go to capital fist </button></a>
    # <br><button><a href=http://127.0.0.1:8000/newlineremove>Go to new line remove </button></a>
    # <br><button><a href=http://127.0.0.1:8000/spaceremove>Go to space remove </button></a>
    # <br><button><a href=http://127.0.0.1:8000/charcount>Go to character count </button></a>
    # ''')


    # Old code   

# def removepunc(request):
#     # Getting the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse('''Remove punc <a href='/'>Back</a>''')

# def capfirst(request):
#     return HttpResponse("Capitalize first <a href='/'>Back</a>")

# def newlineremove(request):
#     return HttpResponse("Removing new line first <a href='/'>Back</a>")

# def spaceremove(request):
#     return HttpResponse("Removing empty or free spaces <a href='/'>Back</a>")

# def charcount(request):
#     return HttpResponse("Counting characters <a href='/'>Back</a>")

                
def analyze(request):
    djtext = request.GET.get('text','default') #ye main textbox ko aik tareeqay sai id dii thi woh check kar rahay hain
    removepunc = request.GET.get('removepunc','off') #isska matlab hai kai kia checkbox mil raha hai if true then value return this 
    capitalize = request.GET.get('capitalize','off')
    newlineremove = request.GET.get('newlineremove','off')
    extraspaceremove = request.GET.get('extraspaceremove','off')
    charcount = request.GET.get('charcount','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*|`_~'''
    if removepunc == 'on':
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
            # Analyze the text
            return render(request, 'analyze.html', params)
                
    elif capitalize == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
            
    elif newlineremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            # Analyze the text
            return render(request, 'analyze.html', params)
                
    elif extraspaceremove == 'on':
        analyzed = ''
        for char in djtext:
            if char != "  ":
                analyzed = analyzed + char
            params = {'purpose': 'Removed Extra space ', 'analyzed_text': analyzed}
            #Analyze the text
            return render(request, 'analyze.html', params)
    
    elif charcount == 'on':
        analyzed = ''
        for char in djtext:
            # djtext = int(djtext)
            analyzed =  len(djtext)
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            # Analyze the text
            return render(request, 'analyze.html', params)
            
                
    else:
        return HttpResponse('Not found')
    

        