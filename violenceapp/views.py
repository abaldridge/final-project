from django.shortcuts import render

from violenceapp.models import State, Tags, Report

def homepage(request):
    reports = Report.objects.order_by('report_date')
    context = {"reports": reports}
    return render(request, 'index.html', context)    

def reportdetail(request, pk):
    report = Report.objects.get(id=pk)
    context = {"report": report}
    return render(request, 'reportdetail.html', context)   
