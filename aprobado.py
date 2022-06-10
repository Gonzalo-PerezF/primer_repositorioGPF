import sys

#Validar si hay dos notas o no...


if len(sys.argv) == 3:


	print(f"nota 1 es: {sys.argv[1]} \n\n")
	print(f"nota 2 es: {sys.argv[1]} \n\n")
	print(sys.argv)
	# if (sys.argv[1] + sys.argv[2] ) / 2 > 7.0:
	# 	print("muy bien")

else:


	print("Paremtros incorrectos")