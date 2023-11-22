from faults_parser_gen import faults_parser_gen
from reportlab.pdfgen.canvas import Canvas
from make_pdf import missing_gen, present_gen, not_matching_gen
import ast

y = 800
canvas = Canvas("output.pdf")
with open("parsed_faults.txt", 'r') as file:
	for line in file:
		element = ast.literal_eval(line)
		element_2 = element[2].replace("\n", " ")
		if element.__len__() == 4:
			element_3 = element[3].replace("\n", " ")
		if element[0] == "missing":
			missing_gen(element[1], element_2, y, canvas)
		elif element[0] == "presented":
			present_gen(element[1], element_2, element_3, y, canvas)
		elif element[0] == "not_matching":
			not_matching_gen(element[1], element_2, element_3, y, canvas)
		y -= 55
		if (y < 55):
			canvas.showPage()
			y = 800
	canvas.save()
