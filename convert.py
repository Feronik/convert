import re
import os
import datetime
import json

roman = {	#Словарь для конвертирования из римских чисел.
	'I': 1, 
	'V': 5, 
	'X': 10, 
	'L': 50, 
	'C': 100, 
	'D': 500, 
	'M': 1000 
}

arab = {	#Словарь для конвертирования из арабских чисел.
	1000: 'M', 
	900: 'CM', 
	500: 'D', 
	400: 'CD', 
	100: 'C', 
	90: 'XC', 
	50: 'L', 
	40: 'XL', 
	10: 'X', 
	9: 'IX', 
	5: 'V', 
	4: 'IV', 
	1: 'I' 
}

def rom (roman_number):					#Функция конвертирования из римских в арабские цифры, принимает в качестве аргумента римское число.
	tmp = 0
	result = 0
	for number in roman_number:
		roman_number = roman[number]  	#В полученный аргумент присваивается значение соответстующее первому символу аргумента согласно словарю roman.
		if roman_number < tmp:			#Условие для конвертирования чисел в порядке которых большая цифра стоит перед меньше, например "VI", "XI", и т.д.
			result += tmp
			tmp = roman_number
		elif roman_number>tmp:			#Условие для конвертирования чисел в порядке которых меньшая цифра стоит перед большей, например "IV", "IX", и т.д.
			if tmp == 0:
				tmp = roman_number
			else:
				result += roman_number - tmp
				tmp = 0
		elif roman_number == tmp:		#Условие для конвертирования чисел в порядке которых подряд стоят одинаковые цифры, например "III", "XIII", и т.д.
			result += tmp + roman_number
			tmp = 0
	return result + tmp 				#Возвращение переменной результата + временной переменной необходимо для первого условия.

def arabic(arab_number): 				#Функция конвертирования из арабских в римские цифры, принимает в качестве аргумента арабское число.
	result = ''
	for arb, romn in arab.items():		#В цикле используется две переменные которые принимают ключ и значение словаря arab соответственно.
		while arab_number >= arb:
			result += romn
			arab_number -= arb
	return result

execution = True	#Переменная-флаг в зависимости от значения которой будет выполняться основной цикл программы или нет.
while execution == True:
	check_number = True #Переменная-флаг с помощью которой организован цикл проверки корректности введенных чисел для конвертировки.
	check_exit = True	#Переменная-флаг с помощью которой организован цикл завершения программы или повторения.	
	print("Convert from roman to arabic - 1")
	print("Convert from arabic to roman - 2")
	try:
		choose = int(input("Your choose 1 or 2: "))
	except ValueError:
		check_number = False
		check_exit = False
		print("\nWrong! Incorrect choose.\n")
	
	while check_number == True:
		if choose == 1:
			num = input("\nEnter roman number: ")
			regex = re.compile(	r'^.*(.)(\1)(\1)(\1).*$')			#Условие для выполнения регулярного выражения. 	
																	#Согласно условию в римском числе не может стоять 4 одинаковые цифры подряд.										
			if regex.match(num):	#Регулярное выражение по поиску соответствий условию в веденных римских числах.
					print("\nWrong! Invalid number format.")
			else:
				try:
					print("\nArabic nubmer: ", rom(num))
					check_number = False
				except KeyError:
					print("\nWrong! The value is not a Roman number.")
		elif choose == 2:
			try:
				num = int(input("\nEnter arabic number: "))
				if num == 0:
					print ("\nRoman numbers not have zero.")
					check_exit == False
				else:
					print("\nRoman nubmer: ", arabic(num))	
					check_number = False
			except ValueError:
				print("\nWrong! Incorrect number.")
		else:
			check_number = False
			check_exit = False
			print("\nWrong! Incorrect choose.\n")
							
	while check_exit == True:						#Если пользователь хочет выйти из программы то по условию основная переменная-флаг execution
		exit_variable = input("\nExit (y/n)?: ")	#меняет своё значение и выходит из основного цикла.
		os.system('cls')							#Очищение консоли, ипользовано с целью не засорять консоль, при необходимости можно убрать.	
		if exit_variable == 'y':
			execution = False
			check_exit = False
		elif exit_variable == 'n':
			check_exit = False
		else:
			print("\nIncorrect choose.")