from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
import time
import mysql.connector


app = Flask(__name__)
'''
@app.route('/')
def hello() -> '302':
    return redirect('/entry')
'''
def log_request(req:'flask_request', res:str) -> None:
	#with open('vsearch.log', 'a') as log:
		#current_time = "%04d-%02d-%02d %02d:%02d:%02d" % (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
		#print(current_time, req.form, req.remote_addr, req.user_agent, res, file = log, sep = '|')
	dbconfig = {'host' : 'localhost',
				'user' : 'root',
				'password' : 'Rmwlrkxsp33$',
				'database' : 'vsearchlogDB', }
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()
	_SQL = """insert into log (phrase, letters, ip, browser_string, results)
				values
				(%s, %s, %s, %s, %s)"""
	cursor.execute(_SQL, (req.form['phrase'],
							req.form['letters'],
							req.remote_addr,
							req.user_agent.browser,
							res, ))
	conn.commit()
	cursor.close()
	conn.close()
	
@app.route('/search4', methods = ['POST'])
def do_search() -> 'html':
	phrase = request.form['phrase']
	letters = request.form['letters']
	results = str(search4letters(phrase, letters))
	log_request(request, results)
	return render_template('results.html', the_title = 'Here are your results:',
                           the_phrase = phrase, the_letters = letters,
                           the_results = results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html', the_title = 'welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
	contents = []
	with open('vsearch.log') as log:
		for line in log:
			contents.append([])
			for item in line.split('|'):
				contents[-1].append(escape(item))
	titles = ('Time', 'Form Data', 'Remote_addr', 'User_agent', 'Results')
	return render_template('viewlog.html',
							the_title = 'View Log',
							the_row_titles = titles,
							the_data = contents,)
	
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0')
