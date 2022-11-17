import datetime as dt

hello = "Hello There! please enter your name and click on GO:"
pyscript.write('hi',hello)
pyscript.write('date',dt.date.today().strftime('%A %B %d, %Y'))

def grafico(*args):	
	import matplotlib.pyplot as plt
	#fig = plt.subplots()
	country = 'Afganistan','Argentina','Australia','Bolivia','Brasil','Canada','Chile','Colombia','Haiti','Japon','Mexico','Venezuela'
	age = [65,77,83,72,76,82,80,77,64,85,75,72]
	fig = plt.figure(figsize=(13,8))
	barras = plt.bar(country,age,color="#7FFFD4")
	plt.xlabel('Pais')
	plt.ylabel('Expectativa de Vida')
	plt.title('Expectativa de vida en algunos paises 2020')	
	#Agrego label a cada barra, usando for y aplicando plt.text: primero y segundo parametro son float, 
	#asi que obtengo el alto y posicion en x de cada barra(y divido entre 2 para ubicar en centro). El tercero es string
	for bar in barras:
		y = bar.get_height()
		x = bar.get_x() + bar.get_width() / 2
		plt.text(x,y,s= str(y),ha = 'center',va = 'bottom')#ha y va son la alineacion vertical y horizontal

	#Encontrar valores Minimo y Maximo del DataSet
	minV, maxV = age[0],age[0]
	for j in range(0,len(age)):
		if age[j] < minV:
			minV = age[j]
			posMin = age.index(minV)
		if age[j] > maxV:
			maxV = age[j]
			posMax = age.index(maxV)
	maxiText = "el maximo es: "+str(maxV)
	minText = "el minimo es: "+str(minV)
	plt.annotate(maxiText,xy=(-0.5,85))
	plt.annotate(minText,xy=(-0.5,82))
	#paso al html el grafico y el Insight usando los indices
	insight = "Lower expectative Country: "+ country[posMin] + "<br>" + "Higher expectative Country: " + country[posMax]
	Element('graficos').write(fig)
	Element('grafInsight').write(insight)


def saludo(*args):
	nombre = Element('name').element.value
	Element('saludo').element.innerHTML = "Greetings <strong>"+ nombre + "!!</strong> Nice to having you here!<br>Could you please tell me, are you interested in Data visualization?"


def interes(*args):
	interesado = Element('interested').element.value
	if interesado == "yes" or interesado == "Yes" or interesado == "si":
		t = "<br>Great! let's take a look at this example: I have created a bar chart using Matplotlib, besides of the graph, it also calculates min and max values and its corresponding Country, this is useful on large datasets"
		Element('interest').element.innerHTML = t
		grafico()		
	elif interesado == "no" or interesado == "No":
		Element('interest').element.innerHTML = "sorry about that, maybe next time"
	else:
		Element('interest').element.innerHTML = "please, write yes or no, thanks"
