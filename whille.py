
salir = 'ho'

while salir != 'salir':

	salir = input('quieres sumar, restar o salir: ')

	if salir == 'sumar':

		primer_numero = int(input('cual es tu primer numero: '))
		segundo_numero = int(input('cual es tu segundo numero: '))

		print (primer_numero + segundo_numero)

	elif salir == 'restar':

		primer_numero = int(input('cual es tu primer numero: '))
		segundo_numero = int(input('cual es tu segundo numero: '))

		print (primer_numero - segundo_numero)

print ('saliste de la calculadora :)')

