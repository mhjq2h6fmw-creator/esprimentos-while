i = int(input('cuantos niveles quieres que tenga tu arbol: '))
c = i 
a = 1
b = 1


while a<i:

	if b<3:

		print(' '* c ,'*'* b)

		b=b*3
		a=a+1
		c=c-1


	elif b==3:

		print(' '* c ,'*'* b)

		b=b+2
		a=a+1
		c=c-1


	elif b>3:

		print(' '* c ,'*'* b)

		b=b+2
		a=a+1
		c=c-1




print('lsito')
