from django.shortcuts import render

# Create your views here.
def home(request):
    res = 0
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        a = int(a)
        b = int(b)
        if c == '+':
            res = a + b
        elif c == '-':
            res = a - b
        elif c == '*':
            c = a * b 
        else:
            try:
                res = a / b 
            except ZeroDivisionError:
                res = "enter number" 
    return render(request, 'main/home.html', context={
        'res':res
    })       