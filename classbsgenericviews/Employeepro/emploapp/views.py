from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Employee
from django.urls import reverse_lazy
# Create your import views here.

class ListEmp(ListView):
    model = Employee
    fields = '__all__'
    paginate_by = 2

class CreateEmp(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'emploapp/employee_form.html'
    success_url = reverse_lazy('list_url')

class DeleteEmp(DeleteView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('list_url')

class UpdateEmp(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('list_url')

from django.http import FileResponse
from fpdf import FPDF

def GeneratePDF(request):
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
   # pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    #pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
   # pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    #pdf.line(10, 30, 150, 30)
    #pdf.line(10, 38, 150, 38)
    lines=[]

    record = Employee.objects.all()

    for f in record:
        lines.append(f.emp_name)
        lines.append(f.profile)
        lines.append(f.salary)
        lines.append(f.email)
        lines.append(" ")
         
    for line in lines:
        pdf.cell(200, 8, f"{line}", 0, 1)

    pdf.output('Employee.pdf', 'F')
    return FileResponse(open('Employee.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

def particularData(request,pk):
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'Employee Details PDF:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    #pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    

    farm = Employee.objects.get(id=pk)
    NM=farm.emp_name
    PF=farm.profile
    SAL=farm.salary
    ML=farm.email
    lines=[NM,PF,SAL,ML]
    
    for line in lines:
        pdf.cell(200, 8,f"{line}", 0, 1)
    pdf.output(f'{NM}.pdf', 'F')
    return FileResponse(open(f'{NM}.pdf', 'rb'), as_attachment=True, content_type='application/pdf')

# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# import io
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

# def GenaratePDF(request):
#     buf = io.BytesIO()
#     c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob = c.beginText()
#     textob.setTextOrigin(inch,inch)
#     textob.setFont('Helvetica', 14)
#     lines =[]
#     farm = Employee.objects.all()

    # for f in farm:
    #     lines.append(f.emp_name)
    #     lines.append(f.profile)
    #     lines.append(f.salary)
    #     lines.append(f.email)
    #     lines.append(" ")

    # for line in lines:
    #     textob.textLine(line)

    # c.drawText(textob)
    # c.showPage()
    # c.save()
    # buf.seek(0)

    # return FileResponse(buf, as_attachment=True, filename='xyz.pdf')
