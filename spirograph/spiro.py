# a class that draws a Spirograph
class Spiro:
	# constructor
	def __init__(self, xc, yc, col, R, r, l):
		# create the turtle object
		self.t = turtle.Turtle()
		# set the cursor shape
		self.t.shape('turtle')
		# set the step in degrees
		self.step = 5
		# set the drawing complete flag
		self.drawingComplete = False

		# set the parameters
		self.setparams(xc, yc, col, R, r, l)

		# initizalize the drawing
		self.restart()

	# set the parameters
	def setparams(self, xc, yc, col, R, r, l):
		# the Spirograph parameters
		self.xc = xc
		self.yc = yc
		self.R = int(R)
		self.r = int(r)
		self.l = l
		self.col = col
		# reduce r/R to its smallest form by dividing with the GCD
		gcdVal = gcd(self.r, self.R)
		self.nRot = self.r//gcdVal
		# get ratio of radii
		self.k = r/float(R)
		# set the color
		self.t.color(*col)
		# store the current angle
		self.a = 0

	# restart the drawing
	def restart(self):
		# set the flag
		self.drawingComplete = False
		# show the turtle
		self.t.showturtle()
		# go to the first point
		self.t.up()
		R, k, l = self.R, self.k, self.l
		a = 0.0
		x = R*((1-k)*math.cos(a) + 1*k*math.cos((1-k)*a/k))
		y = R*((1-k)*math.sin(a) + 1*k*math.sin((1-k)*a/k))
		self.t.setpos(self.xc + x, self.yc + y)
		self.t.down()