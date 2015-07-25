
import course_data
import page_parser

keywords = ["add", "remove", "switch", "display", "exit", "help"]

def exit(loop_var):
	loop_var = False

def help():
	print "This will be replaced with a more helpful message later"

def addTerm(terms, season, year):
	terms.append(course_data.Term(season, year))

def removeTerm(terms, season, year):
	found = False
	print "Are you sure you would like to remove the", season, year, "term?"
	if ynInput():
		for index, item in enumerate(terms):
			if item.getSeason() == season and item.getYear() == year:
				terms.pop(index)
				print "Term successfully removed.\n"
				break
		if not found:
			print "Term not found.\n"
	return found
