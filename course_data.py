# ynInput takes no aguments. It prompts the user as to whether or not they
# would like to continue, returning True if they would.

# ynInput: Void -> Bool
def ynInput():
	answer = raw_input("Would you like to continue? (y/n) ")
	if (answer == 'Y' or answer == 'y'):
		return True
	if (answer == 'N' or answer == 'n'):
		return False
	else:
		print "Please answer with 'y' or 'n' only."
		return ynInput()

########################################################################

class CourseID:
	
	def __init__(self, area, number):
		self.area = area;
		self.number = number;
		
	def getArea(self):
		return self.area
	
	def getNumber(self):
		return self.number
	
	def areSame(self, course_id):
		if self.area == course_id.getArea() and self.number == course_id.getNumber():
			return True
		return False
		
	def printID(self):
		print self.area, self.number
		
########################################################################

class Course:
	
	# __init__ takes arguments relating to course data and stores them
	# in self variables
	
	# __init__: Course Str Str Str Str -> Void
	def __init__(self, area, title, description, number):
		self.id_tag = CourseID(area, number)
		self.title = title
		self.description = description
	
	# Generic accessor functions
	
	def getID(self):
		return self.id_tag
	
	def getTitle(self):
		return self.title
	
	def getDesc(self):
		return self.description
	
	def getNumber(self):
		return self.number
	
	def printCourse(self):
		self.id_tag.printID()
		print self.title, '\n'
		print self.description, '\n'
	
class CourseList:
	
	def __init__(self, courses):
		self.courses = courses
	
	def printCourses(self):
		for item in courses:
			print item.getArea, item.getNumber
	
	def findCourse(self, course_id):
		for index, item in enumerate(self.courses):
			if item.getID().areSame(course_id):
				return index
		return False
	
	def addCourse(self, course):
		self.courses.append(course)
	
	def removeCourse(self, index):
		self.courses.pop(index)
	
	def numCourses(self):
		return len(courses)
	
	def printFull(self):
		for item in self.courses:
			item.printCourse()
		
	def printList(self):
		for item in self.courses:
			item.getID().printID()
			print

########################################################################

class Term:
	
	def __init__(self, season, year):
		self.year = year
		self.season = season
		self.courses = CourseList([])
		self.num_courses = 0
	
	def getSeason(self):
		return self.season
	
	def getYear(self):
		return self.year
	
	def addCourse(self, course):
		if self.num_courses == 5:
			print "Adding another course will put the term over 5 courses. \n"
			if not ynInput():
				return False
		if bool(self.courses.findCourse(course.getID())):
			print "Course already exists in term. \n"
			return False
		self.courses.addCourse(course)
		self.num_courses += 1
		print "Course successfully added."
		return True
	
	def removeCourse(self, courseID):
		index = self.courses.findCourse(courseID)
		if not (bool(index)):
			print "Course does not exist in term"
			return False
		self.courses.removeCourse(index)
		self.num_courses -= 1
		print"Course removed successfully"
		return True
	
	def printTerm(self):
		self.courses.printList()

## testing code
'''
course1 = Course("MATH", "Calculus 2 for Engineering", "Elementary approximation methods: interpolation; Taylor polynomials and remainder; Newton's method, Landau order symbol, applications. Infinite series: Taylor series and Taylor's Remainder Theorem, geometric series, convergence test, power series, applications. Functions of several variables: partial derivatives, linear approximation and differential, gradient and directional derivative, optimization and Lagrange multipliers. Vector-valued functions: parametric representation of curves, tangent and normal vectors, line integrals and applications.", "119")

course2 = Course("MATH", "Calculus 3 for Honours Mathematics", "Calculus of functions of several variables. Limits, continuity, differentiability, the chain rule. The gradient vector and the directional derivative. Taylor's formula. Optimization problems. Mappings and the Jacobian. Multiple integrals in various co-ordinate systems.", "237")

course3 = Course("MATH", "Introduction to Combinatorics", "Introduction to graph theory: colourings, matchings, connectivity, planarity. Introduction to combinatorial analysis: generating series, recurrence relations, binary strings, plane trees.", "239")

course4 = Course("MATH", "Linear Algebra 2 (Advanced Level)", "MATH 245 is an advanced-level version of MATH 235.", "245")

course5 = Course("MATH", "Pre-University Algebra and Geometry", "Topics covered in the course include operations with vectors, scalar multiplications dot and cross products, projections, equations of lines and planes, systems of equations, Gaussian elimination, operations with matrices, determinants, binomial theorem, proof by mathematical induction, complex numbers.", "051")

course6 = Course("MATH", "Linear Algebra for Science", "Vectors in 2- and 3-space and their geometry. Linear equations, matrices and determinants. Introduction to vector spaces. Eigenvalues and diagonalization. Applications. Complex numbers.", "114")

term = Term("Fall", "2015")
term.addCourse(course1)
term.addCourse(course2)
term.addCourse(course3)
term.addCourse(course4)
term.addCourse(course5)
term.addCourse(course6)
term.printTerm()
'''
