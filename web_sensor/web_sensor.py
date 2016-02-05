import os, time
from bottle import route, run, template

def cpu_temp():
    dev = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cpu_temp = dev.read()[5:-3]
    return cpu_temp

@route('/temp')
def temp():
    return cpu_temp()
	
@route('/')
def index():
	return template('main.html')
	
@route('/raphael')
def index():
	return template('raphael.2.1.0.min.js')

@route('/justgage')
def index():
	return template('justgage.1.0.1.min.js')

run(host='0.0.0.0', port=80)