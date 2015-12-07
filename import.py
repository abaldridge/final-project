import os, sys, string, csv, datetime, time, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "violence.settings")


from django.conf import settings

from violenceapp.models import ModelName, AnotherModel, ThirdModel

from django.template.defaultfilters import slugify, urlize

django.setup()

reader = csv.reader(open("violencedata.csv", "rU"), dialect=csv.excel)

reader.next()

for row in reader:

    textexample = row[0]

    integerexample = int(row[1])

    floatexample = float(row[2])

    dateparseexample = time.strptime(row[3], "%m/%d/%Y %H:%M")

    dateexample = datetime.datetime(dateparseexample.tm_year, dateparseexample.tm_mon, dateparseexample.tm_mday)

    modnam, modnamcreated = ModelName.objects.get_or_create(name=row[4], attribute=row[5])

    anothermod, anothermodcreated = AnotherModel.objects.get_or_create(model=modnam, other_attribute=row[7])

    print anothermod


