from faults_parser_gen import faults_parser_gen
from reportlab.pdfgen.canvas import Canvas
from make_pdf import missing_gen, present_gen, not_matching_gen

y = 800
# i = 20
canvas = Canvas("output.pdf")
for element in faults_parser_gen("faults.xlsx", "master.docx"):
	if element[0] == "missing":
		missing_gen(element[1], element[2], y, canvas)
	elif element[0] == "presented":
		present_gen(element[1], element[2], element[3], y, canvas)
	elif element[0] == "not_matching":
		not_matching_gen(element[1], element[2], element[3], y, canvas)
	y -= 55
	if (y < 55):
		canvas.showPage()
		y = 800
	# i -= 1
	# if (i == 0):
	# 	break
canvas.save()
