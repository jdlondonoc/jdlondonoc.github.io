import datetime as dt

hello = "Hello There! please enter your name and click on GO:"
pyscript.write('hi',hello)
pyscript.write('date',dt.date.today().strftime('%A %B %d, %Y'))

def saludo(*args):
	nombre = Element('name').element.value
	Element('saludo').element.innerHTML = "Greetings "+ nombre + "! nice to having you here"