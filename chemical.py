import math
import json 
import numpy as np

with open('ptable.json') as f:
	read = json.load(f)
print("\nW E L C O M E")

def menu():
	print("\n \nPlease type an option (just the number)\n")
	eleccion = int(input("1) Electronegativity difference calculator\n2) Molar mass calculator\n3) Elements General info\n4) Molecular geometry calculator\n5) Boyle law calculator\n6) Charles Law\n7) Avogrado Law\n8) Packing efficiency\n9) Exit\n \n I N P U T: "))
	if eleccion == 1:
		difer_electro()
	elif eleccion == 2:
		masa_molar()
	elif eleccion == 3:
		general_info()
	elif eleccion == 4:
		molecular_geometry()
	elif eleccion == 5:
		ley_boyle()
	elif eleccion == 6:
		charles_law()
	elif eleccion == 7:
		avogrado_law()
	elif eleccion == 8:
		packing_efficiency()
	elif eleccion == 9:
		print('\nSee ya')
		exit()
	else:
		print("Wrong input, try again . . .\n")
		menu()

def difer_electro(): # Funcion para calcular diferencia electronegatividad
	print("Type the chemical symbol of the two elements: ")
	
	element_1 = input("Element I: ")
	element_2 = input("Element I: ")

	for i in read['elements']:
		if i['symbol'] == element_1:
			x1 = i['electronegativity_pauling']
			print('electronegativity ',element_1 , x1)
			break

	for n in read['elements']:
		if n['symbol'] == element_2:
			x2 = n['electronegativity_pauling']
			print('electronegativity ', element_2, x2)
			break
	resultado = abs(x1 - x2)

	print("The electronegativity difference is: ", resultado)

	if resultado < 0.5:
		print("Covalent Bond")
	elif resultado >= 0.5 and resultado < 2.0:
		print("Polar Covalent Bond")
	elif resultado >= 2.0:
		print("Ionic")

	menu()

def masa_molar():
	cantidad_elementos = int(input("Enter int number with number of elements in molecule: "))
	elementos = [] 
	multiplos = []
	umas = []

	for x in range(cantidad_elementos):
		elemento = input("Enter element symbol: ")
		elementos.append(elemento)
		cantidad = int(input("Enter number of atoms: "))
		multiplos.append(cantidad)
		# Buscar elemento en json y sacar su atomic mass. append to other array

		for i in read['elements']:
			if i['symbol'] == elemento:
				uma = i['atomic_mass']
		umas.append(uma)
		print('\n')

	operaciones = sum(np.multiply(multiplos, umas))
	print('\n Resultado: ', operaciones, 'g/mol')
	menu()



def general_info():

	def el_sy(): # Function for printint a menu with the name and symbol
		print('ok')

	print('Type >>menu<< for menu of symbol and element. \n')
	get_element = input('Enter element symbol: ')
	
	if get_element == 'menu':
		el_sy()
	else:
		for i in read['elements']:
			if i['symbol'] == get_element:
				print(i['name'], 
					'\n','atomic_mass: ', i['atomic_mass'], 
					'\n','electronegativity: ', i['electronegativity_pauling'],
					'\n','elctro config: ', i['electron_configuration'],
					'\n','sematic config: ', i['electron_configuration_semantic'],
					'\n','electron affinity: ', i['electron_affinity'],
					'\n','boiling point: ', i['boil'],
					'\n','shells: ', i['shells'])
	menu()

def molecular_geometry():
	number_elements = int(input("Enter number of elements on molecule: "))
	total_e_necessary = []
	number_valance_electrons = []

	for i in range(number_elements):
		element = input("Input symbol of element: ")
		number_atoms = int(input("Numer of atoms from %s: "%(element)))


		# special case Hydrogen. Necessary electrons to be stable
		if element == 'H':
			aj = 2
		else:
			aj = 8
		n_electrons = (aj * number_atoms) / 2 # Result needs to be added to a list to be summed
		total_e_necessary.append(n_electrons)

		# get elements group "xpos"json for valance electrons
		for j in read['elements']:
			if j['symbol'] == element:
				group = j['xpos']

		# if statement to see if is a transition metal
		if group < 3 or group > 12:
			if group > 12:
				group -= 10
				valance_e_atom = (group * number_atoms) / 2
				number_valance_electrons.append(valance_e_atom)
			else:
				# append to number of valance electrons
				valance_e_atom = (group * number_atoms) / 2
				number_valance_electrons.append(valance_e_atom)
		else:
			print('e')

	t_electrons = sum(total_e_necessary)
	print('Total ammount of bonds and lone pairs: ', t_electrons)
	t_valance = sum(number_valance_electrons)
	print('Total ammount of pairs available: ', t_valance)
	no_bonds = t_electrons - t_valance # This is the number pair of bonds necessaary
	print('Total ammount of bonds: ', no_bonds)
	remaining_b = t_valance - no_bonds # remaining lone pairs
	print('Total ammount lone pairs: ', remaining_b)

	menu()

def ley_boyle():
	print("BOYLE LAW \nRelation between volume and pressure")
	variable = input("variable to be calculate(p or v): ")
	if variable == 'p':
		print((float(input('P2 : ')) * float(input('V2 : '))) / float(input('V1 : ')))
	elif variable == 'v':
		print((float(input('P2 : ')) * float(input('V2 : '))) / float(input('P1 : ')))
	else:
		print('error')
	menu()

def charles_law():
	print('CHARLES LAW\n Relation between volume and temperature(Kelvin)')
	variable = input("variable to be calculate(v or t): ")
	if variable == 'v':
		print((float(input('V2: ')) * float(input('T1 : '))) / float(input('T2: ')))
	elif variable == 't':
		print((float(input('V1: ')) * float(input('T2: '))) / float(input('V2 : ')))
	else:
		print('error')
	menu()
def avogrado_law():
	print('AVOGRADO LAW\nRelation between volume and molar mass')
	variable = input('variable to be calculate(v or m): ')
	if variable == 'v':
		print((float(input('V2 : ')) * float(input('n1 : '))) / float(input('n2 : ')))
	elif variable == 'm':
		print((float(input('V1')) * float(input('n2'))) / float(input('V2')))
	else:
		print('error')
	menu()
def packing_efficiency():
	radius = float(input('Enter radius: '))
	unit = radius * 2
	print(((math.pi * (radius)**2)/unit) * 100)
	menu()

menu()