import csv, io
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
        io_string = io.StringIO(file_data)
        # lines = io_string.split("\n")
        
        # idea: count number of entries first before looping

        for lines in csv.reader(io_string):
            # iaccs_id on CSV file cannot be blank
            if lines[0] is '':
                break
            else:
                data_dict = {}
                data_dict['iaccs_id'] = float(lines[0])  #change to whole number
                data_dict['membership_branch'] = Branch.objects.get(branch_name = lines[1])  #change to dynamic
                data_dict['first_name'] = lines[3]
                data_dict['middle_name'] = lines[4]
                data_dict['last_name'] = lines[2]
                data_dict['name_extension'] = lines[5]
                data_dict['address'] = ''
                data_dict['gender'] = ''
                data_dict['civil_status'] = ''
                data_dict['birth_date'] = lines[6]
                data_dict['email'] = ''
                data_dict['role'] = Role.objects.get(role_name__icontains = 'Planholder')
                
                try:
                    form = BioEncodeForm(data_dict)
                    if form.is_valid():
                        if Client.objects.get(first_name = lines[3], last_name = lines[2], middle_name = lines[4]):
                            print('<----duplicate---->')
                            print('%s %s' % lines[3], lines[2])
                            # add statement to add duplicated names to a dictionary
                            # then output to views
                        else:
                            form.save()
                    else:
                        print(form.errors)
                        print('<----inner else---->')
                        break
                except Exception as e:
                    
                    print(form.errors)
                    print('<---- outer try except---->')
                    break
                    
                # file_data.close()
                print('<----data saved---->')
        return HttpResponseRedirect(reverse('home'))