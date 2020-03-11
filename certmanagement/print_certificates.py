from reportlab.rl_settings import defaultPageSize
from reportlab.lib.units import inch
birth_Title = "National Government of Kenya"
birth_page_info = "Birth Certificate"
PAGE_HEIGHT = defaultPageSize[1]
PAGE_WIDTH = defaultPageSize[0]


def birth_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, birth_Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % birth_page_info)
    canvas.restoreState()
