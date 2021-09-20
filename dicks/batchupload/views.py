import csv
from django.db.models.functions import Floor
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from formtools.preview import FormPreview
from .forms import *
from enroller.forms import BioEncodeForm
from enroller.models import *
from enroller.urls import *

# Create your views here.



class ExcelUpload(generic.TemplateView):
    '''
    client upload via backend
    for masterlist 1
    Client ID	BRANCHES	NAMES	DATE OF BIRTH	AGE	AGE BRACKET
    '''
    
    
    def get(self, request, *args, **kwargs):
        template_name = 'create/excel-upload.html'
        form_class = UploadExcelForm
        return render(request, template_name, {'form':form_class})
    
    def post(self, request, *args, **kwargs):
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            print('<----success---->')
            print(Client.objects.get(pk=1))
            request.FILES["file"].save_to_database(
                models = Client,
                mapdicts = [
                    {
                        'iaccs_id':'Client ID',
                        'membership_branch':'',
                        'first_name':'first_name',
                        'middle_name':'middle_name',
                        'last_name':'NAMES',
                        'name_extension':'ext',
                        'address':'',
                        'gender':'',
                        'civil_status':'',
                        'birth_date':'DATE OF BIRTH',
                        'email':'',
                        'role':''
                    }
                ]
            )
            return HttpResponseRedirect(reverse('excel-up'))
        else:
            print('<----error---->')
            # url = reverse('excel-up')
            raise Http404
            
            
            
class UploadCSV(generic.TemplateView):
    '''
    CSV upload only
    '''
    
    def get(self, request, *args, **kwargs):
        template_name = 'create/excel-upload.html'
        form_class = UploadExcelForm
        return render(request, template_name, {'form':form_class})
        
        
    def post(self, request, *args, **kwargs):
        csv_file = request.FILES["file"]
        file_data = csv_file.read().decode("iso-8859-1")
        lines = file_data.split("\n")

        for line in lines:
            lines = file_data.split("\n")
            fields = line.split(",")
            data_dict = {}
            data_dict['iaccs_id'] = int(float(fields[0]))  #change to whole number
            data_dict['membership_branch'] = Branch.objects.get(branch_name = 'Agdao')  #change to dynamic
            data_dict['first_name'] = fields[3]
            data_dict['middle_name'] = fields[5]
            data_dict['last_name'] = fields[2]
            data_dict['name_extension'] = fields[4]
            data_dict['address'] = ''
            data_dict['gender'] = ''
            data_dict['civil_status'] = ''
            data_dict['birth_date'] = fields[9]
            data_dict['email'] = ''
            data_dict['role'] = Role.objects.get(role_name__icontains = 'Planholder')
            
            try:
                form = BioEncodeForm(data_dict)
                if form.is_valid():
                    form.save()
                else:
                    print(form.errors)
                    return HttpResponseRedirect(reverse('csv-up'))
            except Exception as e:
                print(form.errors)
                return HttpResponseRedirect(reverse('csv-up'))
        print('<----data saved---->')
        return HttpResponseRedirect(reverse('home'))