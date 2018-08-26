from flask import escape

def view_the_log() -> str:	
	with open('vsearch.log') as log:
		contents = log.read()
		four_strings = contents.split('|')
		list_test= []
		for i in range(4):
			list_test.append(four_strings[i])
		return print(escape(list_test))

view_the_log()