import urllib
import course_data

def getPage(address):
	return urllib.urlopen(address).read()

def findArea(data):
	index = 0
	while data[index].isalpha() and index < len(data):
		index += 1
	return data[0:index]

def findNumber(data):
	index = 0
	while data[index].isalpha() and index < len(data):
		index += 1
	start = index
	while data[index] != '\"' and index < len(data):
		index += 1
	return data[start:index]

def findTitle(data):
	data = data.split('<b>')
	index = 0
	while data[1][index] != '<' and index < len(data[1]):
		index += 1
	return data[1][0:index]

def findDescription(data):
	data = data.split('colspan=2>')
	index = 0
	while data[2][index] != '<' and index < len(data[2]):
		index += 1
	return data[2][0:index]

def parseCourse(data):
	return course_data.Course(findArea(data), findTitle(data), findDescription(data), findNumber(data))

def parsePage(address):
	data = getPage(address)
	output = ourse_data.CourseList([])
	data = data.split("<center><table border=0 width=80%><tr><td align=left><B><a name = \"")
	data.pop(0)
	for item in data:
		output.addCourse(parseCourse(item))
	return output

## testing code

#testbank = parsePage("http://http://www.ucalendar.uwaterloo.ca/1516/COURSE/course-MATH.html")
#testbank.printList()

def testParse(data):
	output = course_data.CourseList([])
	data = data.split("<center><table border=0 width=80%><tr><td align=left><B><a name = \"")
	data.pop(0)
	for item in data:
		output.addCourse(parseCourse(item))
	return output

data = """
<html><head>
<title>Courses Mathematics </title>

</head>

<body>

</head>
<body link="ff0000" vlink="0000ff"  bgcolor="#FFFFFF">
<table width="100%">
<td valign=top align=left><h3>Course Descriptions - Undergraduate Calendar 2015-2016</h3>

<a href="https://uwaterloo.ca/">University of Waterloo Home</a> |
<a href="http://ugradcalendar.uwaterloo.ca/">Undergraduate Calendar</a> |
<a href="http://ugradcalendar.uwaterloo.ca/default.aspx?pageid=616">Course Description Index</a> |
<a href="http://ugradcalendar.uwaterloo.ca/default.aspx?pageid=10159">Contact Us</a> |
<a href="https://uwaterloo.ca/privacy/">Privacy</a>

<hr>
<td width="20%" valign=top align=center><img
  src="http://uwaterloo.ca/images/template/uw_wordmark.gif"
  alt="University of Waterloo">
<br>
</td>
</table>

<table width="100%" cellpadding=5  vlink="#00FF00" >
<!-- commented  out links so only use ACMS for navigation - Cam McKay - 29th Jan 2009
 <tr>
 <td width="20%" bgcolor="#FF0000" vlink="#00FF00">
 <table  width="100%" >
   <tr><td align=center >
   <a href="http://www.uwaterloo.ca"><font color="#FFFF00" face=helvetica  size="-1"><b>UW&nbsp;&nbsp;HOME</b></font></a>
   </td>
   </table>
   
<td align=center width="20%" bgcolor="#000000">
 <table  width="100%" >
  <tr><td align=center>
  <a href="http://www.ucalendar.uwaterloo.ca/0708/COURSE/index.html"><FONT  face=helvetica  size="-1"
    COLOR="#FFCC00"><b>CALENDAR &nbsp;CONTENTS</b></font></a>
 </table>
</td>


   
<td align=center width="20%" bgcolor="#000000">
 <table  width="100%" >
  <tr><td align=center>
  <a href="index.html"><FONT  face=helvetica  size="-1"
    COLOR="#FFCC00"><b>UNDERGRADUATE COURSE DESCRIPTIONS &nbsp;INDEX</b></font></a>
 </table>
</td>

</table>

-->

</table>



<table width="100%" cellpadding=15  >
<tr>


<td align=center width="20%" bgcolor="#FFFFC6">

<table  width="100%" >

<tr><td align=center><font color="#000000"   size="+2"><b>



M&nbsp;A&nbsp;T&nbsp;H&nbsp;E&nbsp;M&nbsp;A&nbsp;T&nbsp;I&nbsp;C&nbsp;S&nbsp;

</table>
</table>
<!--
<center><img src="http://www.adm.uwaterloo.ca/infoucal/images/new-smalluw.gif"></center>
-->
<p>





 <h4>Notes</h4>


<i>See also Actuarial Science, Applied Mathematics, Combinatorics and 
Optimization, Computer Science, Mathematics Electives, 
Pure Mathematics,
Statistics. </i>
<p>



<p><A name="MATH000S"><h3>MATH 00s</h3></a><br>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH51"></a>MATH 51 LEC 0.00</b></td><td align=right>Course ID: 010374</td></tr><tr><td colspan=2><b>Pre-University Algebra and Geometry</B></td></tr><tr><td colspan=2>Topics covered in the course include operations with vectors, scalar multiplications dot and cross products, projections, equations of lines and planes, systems of equations, Gaussian elimination, operations with matrices, determinants, binomial theorem, proof by mathematical induction, complex numbers.</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Only offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH52"></a>MATH 52 LEC 0.00</b></td><td align=right>Course ID: 010375</td></tr><tr><td colspan=2><b>Pre-University Calculus</B></td></tr><tr><td colspan=2>The concepts included are limits, derivatives, antiderivatives and definite integrals. These concepts will be applied to solve problems of rates of change, maximum and minimum, curve sketching and areas. The classes of functions used to develop these concepts and applications are: polynomial, rational, trigonometric, exponential and logarithmic.</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Only offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH97"></a>MATH 97 LEC 2.50</b></td><td align=right>Course ID: 010113</td></tr><tr><td colspan=2><b>Study Abroad</B></td></tr><tr><td colspan=2>For studies at other universities under approved exchange agreements.</td></tr><tr><td colspan=2><i>Department Consent Required</i></td></tr></table></center><Br><P>
<p><A name="MATH100S"><h3>MATH 100s</h3></a><br>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH103"></a>MATH 103 LEC,TUT 0.50</b></td><td align=right>Course ID: 006847</td></tr><tr><td colspan=2><b>Introductory Algebra for Arts and Social Science</B></td></tr><tr><td colspan=2>An introduction to applications of algebra to business, the behavioural sciences, and the social sciences. Topics will be chosen from linear equations, systems of linear equations, linear inequalities, functions, set theory, permutations and combinations, binomial theorem, probability theory. [Offered: F,W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: Open only to students in the following Faculties: ARTS, AHS, ENV or IS.</i></td></tr><tr><td colspan=2><i> Antireq: 4U Advanced Functions, 4U Mathematics of Data Management, MATH 106, 114, 115, 136, 146, NE 112</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH104"></a>MATH 104 LEC,TUT 0.50</b></td><td align=right>Course ID: 006848</td></tr><tr><td colspan=2><b>Introductory Calculus for Arts and Social Science</B></td></tr><tr><td colspan=2>An introduction to applications of calculus in business, the behavioural sciences, and the social sciences. The models studied will involve polynomial, rational, exponential and logarithmic functions. The major concepts introduced to solve problems are rate of change, optimization, growth and decay, and integration. [Offered: F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: Open only to students in the following Faculties: ARTS, AHS, ENV, SCI.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 127, 137, 147</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH106"></a>MATH 106 LEC,TUT 0.50</b></td><td align=right>Course ID: 006869</td></tr><tr><td colspan=2><b>Applied Linear Algebra 1</B></td></tr><tr><td colspan=2>Systems of linear equations. Matrix algebra. Determinants. Introduction to vector spaces. Applications. [Offered: F,W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 103 or 4U Calculus and Vectors.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 114, 115, 136, 146, NE 112</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH109"></a>MATH 109 LEC,TUT 0.50</b></td><td align=right>Course ID: 006853</td></tr><tr><td colspan=2><b>Mathematics for Accounting</B></td></tr><tr><td colspan=2>Review and extension of differential calculus for functions of one variable. Multivariable differential calculus. Partial derivatives, the Chain Rule, maxima and minima and Lagrange multipliers. Introduction to matrix algebra.</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 104 or 4U Calculus and Vectors; Accounting and Financial Management or Science Biotechnology/CA students only.</i></td></tr><tr><td colspan=2><i> Antireq: ECON 211, MATH 116, 117, 124, 127, 137, 147</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH114"></a>MATH 114 LEC,TUT 0.50</b></td><td align=right>Course ID: 011645</td></tr><tr><td colspan=2><b>Linear Algebra for Science</B></td></tr><tr><td colspan=2>Vectors in 2- and 3-space and their geometry. Linear equations, matrices and determinants. Introduction to vector spaces. Eigenvalues and diagonalization. Applications. Complex numbers. [Offered: F]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors; Science students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 106, 115, 136, 146, NE 112</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH115"></a>MATH 115 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006862</td></tr><tr><td colspan=2><b>Linear Algebra for Engineering</B></td></tr><tr><td colspan=2>Linear equations, matrices and determinants. Introduction to vector spaces. Eigenvalues and diagonalization. Applications. Complex numbers. [Offered: F]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors or 4U Mathematics of Data Management; Engineering students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 106/125, 114, 136, 146, NE 112</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH116"></a>MATH 116 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006865</td></tr><tr><td colspan=2><b>Calculus 1 for Engineering</B></td></tr><tr><td colspan=2>Functions: review of polynomials, exponential, logarithmic, trigonometric. Operations on functions, curve sketching. Trigonometric identities, inverse functions. Derivatives, rules of differentiation. Mean Value Theorem, Newton's Method. Indeterminate forms and L'Hopital's rule, applications. Integrals, approximations, Riemann definite integral, Fundamental Theorems. Applications of the integral. [Offered: F]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors; Open to students in Engineering excluding Electrical and Computer Eng, Nanotechnology Eng, Software Eng and Systems Design Eng.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 117, 124, 127, 137, 147</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH117"></a>MATH 117 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006866</td></tr><tr><td colspan=2><b>Calculus 1 for Engineering</B></td></tr><tr><td colspan=2>Functions of engineering importance; review of polynomial, exponential, and logarithmic functions; trigonometric functions and identities. Inverse functions (logarithmic and trigonometric). Limits and continuity. Derivatives, rules of differentiation; derivatives of elementary functions. Applications of the derivative, max-min problems, Mean Value Theorem. Antiderivatives, the Riemann definite integral, Fundamental Theorems. Methods of integration, approximation, applications, improper integrals. [Offered: F]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors; Open only to students in Electrical and Computer Engineering or Software Engineering or Nanotechnology Engineering.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 116, 124, 127, 137, 147</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH118"></a>MATH 118 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006867</td></tr><tr><td colspan=2><b>Calculus 2 for Engineering</B></td></tr><tr><td colspan=2>Methods of integration: by parts, trigonometric substitutions, partial fractions; engineering applications, approximation of integrals, improper integrals. Linear and separable first order differential equations, applications. Parametric curves and polar coordinates, arc length and area. Infinite sequences and series, convergence tests, power series and applications. Taylor polynomials and series, Taylor's Remainder Theorem, applications. [Offered: W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: One of MATH 116, 117, 127, 137, 147; Open only to students in Engineering excluding students in Electrical and Computer Eng, Nanotechnology Eng, Software Eng and Systems Design Eng.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 119, 128, 138, 148</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH119"></a>MATH 119 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006868</td></tr><tr><td colspan=2><b>Calculus 2 for Engineering</B></td></tr><tr><td colspan=2>Elementary approximation methods: interpolation; Taylor polynomials and remainder; Newton's method, Landau order symbol, applications. Infinite series: Taylor series and Taylor's Remainder Theorem, geometric series, convergence test, power series, applications. Functions of several variables: partial derivatives, linear approximation and differential, gradient and directional derivative, optimization and Lagrange multipliers. Vector-valued functions: parametric representation of curves, tangent and normal vectors, line integrals and applications. [Offered: W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: One of MATH 116, 117, 127, 137, 147; Open only to students in Electrical and Computer Engineering or Software Engineering or Nanotechnology Engineering.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 118, 128, 138, 148</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH124"></a>MATH 124 LEC,TUT 0.50</b></td><td align=right>Course ID: 012879</td></tr><tr><td colspan=2><b>Calculus and Vector Algebra for Kinesiology</B></td></tr><tr><td colspan=2>Review of trigonometry and basic algebra. Introduction to vectors in 2- and 3-space: sums, addition, dot products, cross products and angles between vectors. Solving linear systems in two and three variables. Functions of a real variable: powers, rational functions, trigonometric, exponential and logarithmic functions, their properties. Intuitive discussion of limits and continuity. Derivatives of elementary functions, derivative rules; applications to curve sketching, optimization. Relationships between distance, velocity and acceleration. The definite integral, antiderivatives, the Fundamental Theorem of Calculus; change of variable and integration by parts; applications to area, centre of mass. [Offered: F]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Advanced Functions; Kinesiology students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 109, 116, 117, 127, 137, 147</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH127"></a>MATH 127 LEC,TUT 0.50</b></td><td align=right>Course ID: 006871</td></tr><tr><td colspan=2><b>Calculus 1 for the Sciences</B></td></tr><tr><td colspan=2>Functions of a real variable: powers, rational functions, trigonometric, exponential and logarithmic functions, their properties and inverses. Intuitive discussion of limits and continuity. Definition and interpretation of the derivative, derivatives of elementary functions, derivative rules and applications. Riemann sums and other approximations to the definite integral. Fundamental Theorems and antiderivatives; change of variable. Applications to area, rates, average value. [Offered: F,W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 104 or 4U Calculus and Vectors.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 109, 116, 117, 124, 137, 147</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH128"></a>MATH 128 LEC,TUT 0.50</b></td><td align=right>Course ID: 006872</td></tr><tr><td colspan=2><b>Calculus 2 for the Sciences</B></td></tr><tr><td colspan=2>Transforming and evaluating integrals; application to volumes and arc length; improper integrals. Separable and linear first order differential equations and applications. Introduction to sequences. Convergence of series; Taylor polynomials, Taylor's Remainder Theorem, Taylor series and applications. Parametric/vector representation of curves; particle motion and arc length. Polar coordinates in the plane. [Offered: F,W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: One of MATH 117, 127, 137, 147.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 118, 119, 138, 148</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH135"></a>MATH 135 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006878</td></tr><tr><td colspan=2><b>Algebra for Honours Mathematics</B></td></tr><tr><td colspan=2>An introduction to the language of mathematics and proof techniques through a study of the basic algebraic systems of mathematics: the integers, the integers modulo n, the rational numbers, the real numbers, the complex numbers and polynomials. </td></tr><tr><td colspan=2><i>[Note: Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors or 4U Mathematics of Data Management; Honours Mathematics or Mathematics/ELAS or Software Engineering students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 145</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH136"></a>MATH 136 LAB,LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006879</td></tr><tr><td colspan=2><b>Linear Algebra 1 for Honours Mathematics</B></td></tr><tr><td colspan=2>Systems of linear equations, matrix algebra, elementary matrices, computational issues. Real n-space, vector spaces and subspaces, basis and dimension, rank of a matrix, linear transformations and matrix representations. Determinants, eigenvalues and diagonalization, applications. </td></tr><tr><td colspan=2><i>[Note: Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 135 with a grade of at least 60% or MATH 145; Honours Mathematics or Mathematics/ELAS or Mathematical Physics students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 106, 114, 115, 146, NE 112</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH137"></a>MATH 137 LAB,LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006880</td></tr><tr><td colspan=2><b>Calculus 1 for Honours Mathematics</B></td></tr><tr><td colspan=2>Rational, trigonometric, exponential, and power functions of a real variable; composites and inverses. Absolute values and inequalities. Limits and continuity. Derivatives and the linear approximation. Applications of the derivative, including curve sketching, optimization, related rates, and Newton's method. The Mean Value Theorem and error bounds. Introduction to the Riemann Integral and approximations. Antiderivatives and the Fundamental Theorem. Change of variable, areas and rate integrals. Suitable topics are illustrated using computer software. </td></tr><tr><td colspan=2><i>[Note: Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors; Honours Mathematics or Mathematics/ELAS or Mathematical Physics students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 116, 117, 124, 127, 147</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH138"></a>MATH 138 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006881</td></tr><tr><td colspan=2><b>Calculus 2 For Honours Mathematics</B></td></tr><tr><td colspan=2>Review of the Fundamental Theorem. Methods of integration. Further applications of the integral. Improper integrals. Linear and separable differential equations and applications. Vector (parametric) curves in R2. Convergence of sequences and series. Tests for convergence. Functions defined as power series. Taylor polynomials, Taylor's Theorem, and polynomial approximation. Taylor series. Suitable topics are illustrated using computer software. </td></tr><tr><td colspan=2><i>[Note: Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 127 with a grade of at least 70% or MATH 137 with a grade of at least 60% or MATH 147; Honours Mathematics or Mathematics/ELAS or Mathematical Physics students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 118, 119, 128, 148</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH145"></a>MATH 145 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006886</td></tr><tr><td colspan=2><b>Algebra (Advanced Level)</B></td></tr><tr><td colspan=2>MATH 145 is an advanced-level version of MATH 135. [Offered: F]</td></tr><tr><td colspan=2><i>Department Consent Required</i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors or 4U Mathematics of Data Management; Honours Mathematics students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 135</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH146"></a>MATH 146 LAB,LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006887</td></tr><tr><td colspan=2><b>Linear Algebra 1 (Advanced level)</B></td></tr><tr><td colspan=2>MATH 146 is an advanced-level version of MATH 136. [Offered: W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 145; Honours Mathematics students only. </i></td></tr><tr><td colspan=2><i> Antireq: MATH 106, 114, 115, 136, NE 112</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH147"></a>MATH 147 LAB,LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006888</td></tr><tr><td colspan=2><b>Calculus 1 (Advanced Level)</B></td></tr><tr><td colspan=2>MATH 147 is an advanced-level version of MATH 137. [Offered: F]</td></tr><tr><td colspan=2><i>Department Consent Required</i></td></tr><tr><td colspan=2><i>Prereq: 4U Calculus and Vectors; Honours Mathematics students only. </i></td></tr><tr><td colspan=2><i> Antireq: MATH 116, 117, 124, 127, 137</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH148"></a>MATH 148 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006889</td></tr><tr><td colspan=2><b>Calculus 2 (Advanced Level)</B></td></tr><tr><td colspan=2>MATH 148 is an advanced-level version of MATH 138. [Offered: W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 147; Honours Mathematics students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 118, 119, 128, 138</i></td></tr><p></table></center><Br><P>
<p><A name="MATH200S"><h3>MATH 200s</h3></a><br>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH207"></a>MATH 207 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 013105</td></tr><tr><td colspan=2><b>Calculus 3 (Non-Specialist Level)</B></td></tr><tr><td colspan=2>Multivariable functions and partial derivatives. Gradients. Optimization including Lagrange multipliers. Polar coordinates. Multiple integrals. Surface integrals on spheres and cylinders. Introduction to Fourier Series. [Offered: F,W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 128 or 138 or 148.</i></td></tr><tr><td colspan=2><i> Antireq: AMATH 231, MATH 212, 212N, 217, 227, 237, 247</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH211"></a>MATH 211 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006891</td></tr><tr><td colspan=2><b>Advanced Calculus 1 for Electrical and Computer Engineers</B></td></tr><tr><td colspan=2>Fourier series. Ordinary differential equations. Laplace transform. Applications to linear electrical systems. [Offered: F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 119; Not open to Mathematics students.</i></td></tr><tr><td colspan=2><i> Antireq: AMATH 350, MATH 218, 228</i></td></tr><tr><td colspan=2><i>(Cross-listed with ECE 205)</i></td></tr><P></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH212"></a>MATH 212 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006892</td></tr><tr><td colspan=2><b>Advanced Calculus 2 for Electrical Engineers</B></td></tr><tr><td colspan=2>Triple integrals, cylindrical and spherical polar coordinates. Divergence and curl, applications. Surface integrals, Green's, Gauss' and Stokes' theorems, applications. Complex functions, analytic functions, contour integrals, Cauchy's integral formula, Laurent series, residues. [Offered: F,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 211/ECE 205; Not open to Mathematics students.</i></td></tr><tr><td colspan=2><i> Antireq: AMATH 231, MATH 207, 217, 227, 237, 247</i></td></tr><tr><td colspan=2><i>(Cross-listed with ECE 206)</i></td></tr><P></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH213"></a>MATH 213 LEC,TUT 0.50</b></td><td align=right>Course ID: 011849</td></tr><tr><td colspan=2><b>Advanced Mathematics for Software Engineers</B></td></tr><tr><td colspan=2>Fourier series. Differential equations. Laplace transforms. Applications to circuit analysis. [Offered: S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 119; Software Engineering students only.</i></td></tr><tr><td colspan=2><i> Antireq: AMATH 250, MATH 211/ECE 205, MATH 212N, 218, 228</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH215"></a>MATH 215 LEC,TUT 0.50</b></td><td align=right>Course ID: 013464</td></tr><tr><td colspan=2><b>Linear Algebra for Engineering</B></td></tr><tr><td colspan=2>Systems of linear equations; their representation with matrices and vectors; their generalization to linear transformations on abstract vector spaces; and the description of these linear transformations through quantitative characteristics such as the determinant, the characteristic polynomial, eigenvalues and eigenvectors, the rank, and singular values. [Offered F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: Level at least 2A Computer Engineering or Electrical Engineering students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 106, 114, 115, 136, 146, NE 112</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH217"></a>MATH 217 LEC,TUT 0.50</b></td><td align=right>Course ID: 006897</td></tr><tr><td colspan=2><b>Calculus 3 for Chemical Engineering</B></td></tr><tr><td colspan=2>Curves and surfaces in R3. Multivariable functions, partial derivatives, the chain rule, gradients. Optimization, Lagrange Multipliers. Double and triple integrals, change of variable. Vector fields, divergence and curl. Vector integral calculus: Green's theorem, the Divergence theorem and Stokes' theorem. Applications in engineering are emphasized. [Offered: F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 118; Not open to Mathematics students.</i></td></tr><tr><td colspan=2><i> Antireq: AMATH 231, CIVE 221, ENVE 221, MATH 207, 212/ECE 206, MATH 212N, 227, 237, 247, ME 201</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH218"></a>MATH 218 LEC,TUT 0.50</b></td><td align=right>Course ID: 006898</td></tr><tr><td colspan=2><b>Differential Equations for Engineers</B></td></tr><tr><td colspan=2>First order equations, second order linear equations with constant coefficients, series solutions, the Laplace transform method, systems of linear differential equations. Applications in engineering are emphasized. [Offered: F,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: One of MATH 118, 119, 128, 138, 148, SYDE 112; Engineering or Earth Science students only. </i></td></tr><tr><td colspan=2><i> Antireq: AMATH 250, 251, 350, 351, CIVE 222, ENVE 223, MATH 211/ECE 205, MATH 212N, 228, ME 203, SYDE 211</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH225"></a>MATH 225 LEC,TUT 0.50</b></td><td align=right>Course ID: 006870</td></tr><tr><td colspan=2><b>Applied Linear Algebra 2</B></td></tr><tr><td colspan=2>Vector spaces. Linear transformations and matrices. Inner products. Eigenvalues and eigenvectors. Diagonalization. Applications. [Offered: F,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 106 or 136 or 146.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 235, 245</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH227"></a>MATH 227 LEC,TUT 0.50</b></td><td align=right>Course ID: 006907</td></tr><tr><td colspan=2><b>Calculus 3 for Honours Physics</B></td></tr><tr><td colspan=2>Directional derivative and the chain rule for multivariable functions. Optimization, Lagrange multipliers. Double and triple integrals on simple domains; transformations and Jacobians; change of variable in multiple integrals. Vector fields, divergence and curl. Vector integral calculus: Line and surface integrals, Green's Theorem, Stokes' Theorem, Gauss' Theorem, conservative vector fields.</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 128 or 138; Not open to Mathematics students.</i></td></tr><tr><td colspan=2><i> Antireq: AMATH 231, MATH 207, 212/ECE 206, MATH 212N, 217, 237, 247</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH228"></a>MATH 228 LEC,TUT 0.50</b></td><td align=right>Course ID: 006908</td></tr><tr><td colspan=2><b>Differential Equations for Physics and Chemistry</B></td></tr><tr><td colspan=2>First-order equations, second-order linear equations with constant coefficients, series solutions and special functions, the Laplace transform method. Applications in physics and chemistry are emphasized. [Offered: F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 128 or 138; Not open to Mathematics students. </i></td></tr><tr><td colspan=2><i> Antireq: AMATH 250, 251, 350</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH229"></a>MATH 229 LEC,TUT 0.50</b></td><td align=right>Course ID: 013104</td></tr><tr><td colspan=2><b>Introduction to Combinatorics (Non-Specialist Level)</B></td></tr><tr><td colspan=2>Introduction to graph theory: colourings, connectivity, Eulerian tours, planarity. Introduction to combinatorial analysis: elementary counting, generating series, binary strings. [Offered: F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: (MATH 106 or 136 or 146) and (MATH 135 or 145).</i></td></tr><tr><td colspan=2><i> Antireq: CO 220, MATH 239, 249</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH235"></a>MATH 235 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006913</td></tr><tr><td colspan=2><b>Linear Algebra 2 for Honours Mathematics</B></td></tr><tr><td colspan=2>Orthogonal and unitary matrices and transformations. Orthogonal projections, Gram-Schmidt procedure, best approximations, least-squares. Inner products, angles and orthogonality, orthogonal diagonalization, singular value decomposition, applications. </td></tr><tr><td colspan=2><i>[Note: Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 106/125 with a grade of at least 70% or MATH 136 with a grade of at least 60% or MATH 146; Honours Mathematics or Mathematical Physics students.</i></td></tr><tr><td colspan=2><i> Coreq: MATH 128 or 138 or 148.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 225/126, 245</i></td></tr><tr><td colspan=2><i><a href = "http://de.uwaterloo.ca/courses"><b>Also offered Online</b></a></td></tr></i></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH237"></a>MATH 237 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006914</td></tr><tr><td colspan=2><b>Calculus 3 for Honours Mathematics</B></td></tr><tr><td colspan=2>Calculus of functions of several variables. Limits, continuity, differentiability, the chain rule. The gradient vector and the directional derivative. Taylor's formula. Optimization problems. Mappings and the Jacobian. Multiple integrals in various co-ordinate systems. </td></tr><tr><td colspan=2><i>[Note: MATH 247 may be substituted for MATH 237 whenever the latter is a plan requirement. Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: (MATH 106/125 with at least 70% or MATH 136 with at least 60% or MATH 146) and (MATH 128 with at least 70% or MATH 138 with at least 60% or MATH 148); Honours Math or Math/Physics students.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 207, 212/ECE 206, MATH 212N, 217, 227</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH239"></a>MATH 239 LEC,TST,TUT 0.50</b></td><td align=right>Course ID: 006915</td></tr><tr><td colspan=2><b>Introduction to Combinatorics</B></td></tr><tr><td colspan=2>Introduction to graph theory: colourings, matchings, connectivity, planarity. Introduction to combinatorial analysis: generating series, recurrence relations, binary strings, plane trees. </td></tr><tr><td colspan=2><i>[Note: Offered: F,W,S]</i></td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: ((MATH 106 with a grade of at least 70% or MATH 136 or 146) and (MATH 135 with a grade of at least 60% or MATH 145)) or level at least 2A Software Engineering; Honours Mathematics students only.</i></td></tr><tr><td colspan=2><i> Antireq: CO 220, MATH 229, 249</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH245"></a>MATH 245 LEC,TST 0.50</b></td><td align=right>Course ID: 006920</td></tr><tr><td colspan=2><b>Linear Algebra 2 (Advanced Level)</B></td></tr><tr><td colspan=2>MATH 245 is an advanced-level version of MATH 235. [Offered: F,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 146; Honours Mathematics students only.</i></td></tr><tr><td colspan=2><i> Antireq: MATH 225/126, 235</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH247"></a>MATH 247 LEC,TST 0.50</b></td><td align=right>Course ID: 006921</td></tr><tr><td colspan=2><b>Calculus 3 (Advanced Level)</B></td></tr><tr><td colspan=2>Topology of real n-dimensional space: completeness, closed and open sets, connectivity, compact sets, continuity, uniform continuity. Differential calculus on multivariable functions: partial differentiability, differentiability, chain rule, Taylor polynomials, extreme value problems. Riemann integration: Jordan content, integrability criteria, Fubini's theorem, change of variables. Local properties of continuously differentiable functions: open mapping theorem, inverse function theorem, implicit function theorem. [Offered: F,W,S]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: MATH 146, 148; Honours Mathematics students only</i></td></tr><p></table></center><Br><P>
<center><table border=0 width=80%><tr><td align=left><B><a name = "MATH249"></a>MATH 249 LEC,TST 0.50</b></td><td align=right>Course ID: 006922</td></tr><tr><td colspan=2><b>Introduction to Combinatorics (Advanced Level)</B></td></tr><tr><td colspan=2>MATH 249 is an advanced-level version of MATH 239. [Offered: F,W]</td></tr><tr><td colspan=2><i> </i></td></tr><tr><td colspan=2><i>Prereq: (MATH 136 or 146) and (MATH 138 or 148); Honours Mathematics students only.</i></td></tr><tr><td colspan=2><i> Antireq: CO 220, MATH 229, 239</i></td></tr><p></table></center><Br><P>
<table width="100%" cellpadding=5  vlink="#00FF00" >
<!-- commented  out links so only use ACMS for navigation - Cam McKay - 29th Jan 2009
 <tr>
 <td width="20%" bgcolor="#FF0000" vlink="#00FF00">
 <table  width="100%" >
   <tr><td align=center >
   <a href="http://www.uwaterloo.ca"><font color="#FFFF00" face=helvetica  size="-1"><b>UW&nbsp;&nbsp;HOME</b></font></a>
   </td>
   </table>
   
<td align=center width="20%" bgcolor="#000000">
 <table  width="100%" >
  <tr><td align=center>
  <a href="http://www.ucalendar.uwaterloo.ca/0708/COURSE/index.html"><FONT  face=helvetica  size="-1"
    COLOR="#FFCC00"><b>CALENDAR &nbsp;CONTENTS</b></font></a>
 </table>
</td>


   
<td align=center width="20%" bgcolor="#000000">
 <table  width="100%" >
  <tr><td align=center>
  <a href="index.html"><FONT  face=helvetica  size="-1"
    COLOR="#FFCC00"><b>UNDERGRADUATE COURSE DESCRIPTIONS &nbsp;INDEX</b></font></a>
 </table>
</td>

</table>

-->

</table>



</b></table></table>
<!-- <hr>
<p align=center>

The Undergraduate Calendar is published by the
<br> Office of the Registrar, University of Waterloo,
Waterloo, ON N2L 3G1 Canada
<br>
<i>Inquiries:</i>  <a href="mailto:roucal@uwaterloo.ca">roucal@uwaterloo.ca</a><br> -->

 </body></html>


</body>
</html>"""

testParse(data).printFull()
