from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from django.core.files.storage import FileSystemStorage
from reportlab.rl_settings import defaultPageSize
from haystack.query import SearchQuerySet
from io import BytesIO
from reportlab.pdfgen import canvas
"""def print_birth_certificate(request, id):
    applicant = get_object_or_404(BirthRegistration, id=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename='"'+applicant.first_name + '_'+applicant.surname + '_'+applicant.birth_cert_no + '.pdf"''
    buffer = BytesIO()
    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 850, birth_Title)
    p.drawString(100, 800, birth_page_info)
    p.drawString(50, 700, "First Name:" + applicant.first_name)
    p.drawString(200, 700, "Middle Name:" + applicant.first_name)
    p.drawString(100, 600, "Hello world.")
    p.drawString(100, 500, "Hello world.")
    p.drawString(100, 400, "Hello world.")
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly.
    p.showPage()
    p.save()
    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response"""


"""def print_birth_certificate(request, id):
    applicant = get_object_or_404(BirthRegistration, id=id)
    doc = SimpleDocTemplate('/tmp/'+applicant.first_name + '_'+applicant.surname + '_'+applicant.birth_cert_no + '.pdf')
    styles = getSampleStyleSheet()
    Story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]
    # for i in range(100):
    bogustext = ("This is Paragraph number") * 20
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story)
    fs = FileSystemStorage("/tmp")
    with fs.open(applicant.first_name + '_'+applicant.surname + '_'+applicant.birth_cert_no + '.pdf') as pdf:
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename='"+applicant.first_name + '_'+applicant.surname + '_'+applicant.birth_cert_no + '.pdf"''
        return response
    return response"""


"""def birth_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(BirthRegistration).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
            return render(request, 'cert_management/birth_cert/search.html', {'form': form, 'cd': cd,
                                                                              'results': results,
                                                                              'total_results': total_results})"""

