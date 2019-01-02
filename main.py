from bottle import route, run, template, static_file, get, post, delete, request,response
from sys import argv
import json
import pymysql
import os



connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='store',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='localhost', port=os.environ.get('PORT', 7000))
#run(host='0.0.0.0', port=argv[1])
