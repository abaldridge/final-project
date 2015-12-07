import os, sys, string, csv, datetime, time, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "violence.settings")


from django.conf import settings

from violenceapp.models import State, Report

from django.template.defaultfilters import slugify, urlize

django.setup()

reader = csv.reader(open("ViolenceData.csv", "rU"), dialect=csv.excel)

reader.next()

for row in reader:

    nm = row[0]

    ag = int(row[1])

    st = row[2]

    stat, statcreated = State.objects.get_or_create(state_name=st, state_slug=slugify(st))

    dateparseexample = time.strptime(row[3], "%m/%d/%y")

    dateexample = datetime.datetime(dateparseexample.tm_year, dateparseexample.tm_mon, dateparseexample.tm_mday)

    rpt, rptcreated = Report.objects.get_or_create(name=nm, age=ag, state=stat, report_date=dateexample, description=row[4])

    print rpt


