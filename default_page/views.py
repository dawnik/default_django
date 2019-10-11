from django.shortcuts import render

def index(request):
    return render(request, 'default_page/index.html')

def render_context_in_page(request):
    my_title = "Hello there..."
    return render(request, 'default_page/render_context_in_page.html', {"title": my_title})

def render_context_in_page_method_2(request):
    return render(request, 'render_context_in_page_method_2.html')
