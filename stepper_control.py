#!/usr/bin/python37all


import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
s1 = form.getvalue("slider")
button = form.getvalue("zero")
if (button == "Submit"):
  button = 1
else:
  button = 0


with open('stepper_control.txt', 'w') as f:
  f.write(s1)
  f.write('\n')
  f.write(button)
  

print('Content-type:text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/angle_zero.py" method="POST">')
print('<input type="range" name="slider" min="0" max="360" value="%s"><br>' % s1)
print('<input type="submit" value="Select Angle"><br>')
print('Angle = %s' % s1)
print('<br>')
print('Press Submit to Zero')
print('<input type="submit" name="zero" value="Submit"><br>')
print('</form>')
print('</html>')  
