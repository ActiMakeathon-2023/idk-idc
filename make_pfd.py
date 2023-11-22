from reportlab.pdfgen.canvas import Canvas

def missing_gen(number, faultname, y):
	text = str(number) + " : " + faultname + " - Test missing"
	canvas.drawString(72, y, text)

def unsafe_gen(number, faultname, y):
	text = str(number) + " : " + faultname + " - Test not safe"
	canvas.drawString(72, y, text)

def not_matching_gen(number, faultname, testname, y):
	text = str(number) + " : " + faultname + ", " + testname + " - Test not matching"
	canvas.drawString(72, y, text)

canvas = Canvas("test.pdf")
y = 800
for number, faultname in [[123, "name"], [234, "aaa"]]:
	missing_gen(number, faultname, y)
	y -= 36
not_matching_gen(123, "name", "testname", y)
canvas.save()
