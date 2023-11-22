from reportlab.pdfgen.canvas import Canvas

def present_gen(number, faultname, testname, y, canvas):
	text = str(number) + " : Test presented"
	canvas.drawString(20, y, text)
	text = "Faultname: " + faultname
	canvas.drawString(20, y - 15, text)
	text = "Testname: " + testname
	canvas.drawString(20, y - 30, text)

def missing_gen(number, faultname, y, canvas):
	text = str(number) + " : Test missing"
	canvas.drawString(20, y, text)
	text = "Faultname: " + faultname
	canvas.drawString(20, y - 15, text)
	text = "Testname: not found"
	canvas.drawString(20, y - 30, text)

def unsafe_gen(number, faultname, y, canvas):
	text = str(number) + " : Test unsafe"
	canvas.drawString(20, y, text)
	text = "Faultname: " + faultname
	canvas.drawString(20, y - 15, text)
	text = "Testname: " + testname
	canvas.drawString(20, y - 30, text)

def not_matching_gen(number, faultname, testname, y, canvas):
	text = str(number) + " : Test not matching"
	canvas.drawString(20, y, text)
	text = "Faultname: " + faultname
	canvas.drawString(20, y - 15, text)
	text = "Testname: " + testname
	canvas.drawString(20, y - 30, text)

