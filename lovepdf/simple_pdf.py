from fpdf import FPDF

class SimplePdf:
    def __init__(self, text, img_path):
        self.text = text
        self.img_path = img_path
        self.pdf = FPDF(format="A4")

    def create(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=20)
        self.pdf.set_fill_color(91, 139, 181)
        self.pdf.cell(0, 30, txt=self.text, ln=1, align="C", fill=True)

        self.pdf.image(self.img_path, h=70, w=150, x=30, y=50, type="png")

    def save_pdf(self, file_name_out):
        self.pdf.output(file_name_out)
