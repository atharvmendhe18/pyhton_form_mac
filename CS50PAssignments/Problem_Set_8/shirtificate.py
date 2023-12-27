from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.image('shirtificate.png', x=0, y=40)
pdf.set_font("helvetica", "B", 28)
pdf.set_text_color(255, 255, 255)
width = pdf.get_string_width("Atharv Mendhe took CS50") + 6
starting_x = ((210 - width) / 2)
print(starting_x)
pdf.set_x(starting_x)
pdf.cell(0, 200, "Atharv Mendhe took CS50", align="L")
pdf.output('firsttry.pdf')
