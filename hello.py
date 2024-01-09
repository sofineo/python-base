#!/usr/bin/env python3
#SHEBANG - message sent to your OS before starting the file
"""#Here it is the documentation#
Hello World Multi Language

#One sentance about your program
Depending of which language the enviroment is written on the program will print 
the correpondent message.
#Best pratice: Max column is 79!#

Usage:

The variable LANG must be already configured:

	export LANG=en_US

Execution:

	python3 hello.py
	or
	./hello.py 
"""
#Meta data:
__version__ = "0.0.1"
__author__ = "Sofia Neo"
__license__ = "Unlicense"
#Dunder substitute "double under / underline underline = two underline on
#begining and in the end"

import os 

#Define the main block
#if __name__ == "__main__":


current_language = os.getenv("LANG", "en_US")[:5]
#snake case

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "es_SP":
	msg = "Hola, Mundo!"
elif current_language == "fr_FR":
	msg = "Bonjour, Monde!"

print(msg)
