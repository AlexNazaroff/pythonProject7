#!/usr/bin/env python3
import cgi
our_form = cgi.FieldStorage()
in_name = our_form.getfirst('in_name','Значение не задано!')
in_comment = our_form.getfirst('in_comment','Значение не задано')


#print('Content-type: text/html')
print()
#print('<h2>Frexit in Fr</h2>')
print(in_name)
print(in_comment)