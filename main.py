import datetime as dt

hello = "Hello There! please enter your name and click on GO:"
pyscript.write('hi',hello)
pyscript.write('date',dt.date.today().strftime('%A %B %d, %Y'))

def saludo(*args):
	nombre = Element('name').element.value
	Element('saludo').element.innerHTML = "Greetings <strong>"+ nombre + "!</strong> Nice to having you here!<br>Could you please tell me, are you interested in Data visualization?"


def interes(*args):
	interesado = Element('interested').element.value
	if interesado == "yes":
		Element('interest').element.innerHTML = "Great! let's take a look at some examples"
	elif interesado == "no":
		Element('interest').element.innerHTML = "sorry about that, maybe next time"
	else:
		Element('interest').element.innerHTML = "please, write yes or no, thanks"