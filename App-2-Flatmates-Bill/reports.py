import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    generate pdf report giving out infor about flatmates period bill share name
    """
    def __init__(self, name):
        self.name = name

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='c', ln=1)

        # Insert period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Name and bill share
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate2))), border=1, ln=1)

        # Name and bill share
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=str(round(flatmate1.pays(bill, flatmate1))), border=1, ln=1)

        # Change directory to files and open pdf

        os.chdir('files')
        pdf.output(self.name)
        webbrowser.open(self.name)
