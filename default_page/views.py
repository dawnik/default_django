from django.shortcuts import render

def index(request):
    return render(request, 'default_page/index.html')

def render_context_in_page(request):
    my_title = "Hello there..."
    context = {"title": "my title,"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, 'default_page/render_context_in_page.html', context)

def render_context_in_page_method_2(request):
    return render(request, 'render_context_in_page_method_2.html')
