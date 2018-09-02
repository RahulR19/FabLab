from django.shortcuts import render
from django.template import Context
from personal.forms import ReserveForm
from personal.forms import CancelForm
from personal.models import Reserve
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'personal/FL.html')

def reserve(request):

    if request.POST:
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
        print(form)
        print(request.POST)
        print(request.POST.get("Rollno"))
        return HttpResponseRedirect('I.html')
    return render(request, 'personal/R.html')
    """else:
         form = Res()
         args = {'forms': form}"""


def cancel(request):

    if request.POST:
        if Reserve.objects.filter(Rollno = request.POST.get("Rollno") , Pin = request.POST.get("Pin")) :
            Reserve.objects.filter(Rollno = request.POST.get("Rollno") , Pin = request.POST.get("Pin")).delete()
            return HttpResponseRedirect('C2.html')
        else:
            return render(request, 'personal/C1.html')
    return render(request, 'personal/C.html')

def items(request):
    if request.POST:
        print(request.POST)
        Reserve.objects.filter(Instrument="No Instrument Selected").update(Instrument=request.POST.get("Instrument"))
        return HttpResponseRedirect('I1.html')
    return render(request, 'personal/I.html')


def about(request):
    return render(request, 'personal/A.html')

def itemsuccess(request):
    return render(request, 'personal/I1.html')

def cancelsuccess(request):
    return render(request, 'personal/C2.html')

"""
 def studentlist():
     pwd = os.path.dirname(__file__)
     file = open(pwd + '/students.csv')
     data = file.readlines()
     file.close()
     students = []
     for row in data:
         a = row.split(',')
         a[3] = a[3].replace('\n', '')
         students.append(a)
     students.pop(0)
     return students """
