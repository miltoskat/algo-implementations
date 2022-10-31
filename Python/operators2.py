#!/usr/local/bin/python3.6

while 1:
	a=int(input("Δώσε τον πρώτο αριθμό: "))
	print()
	b=int(input("Δώσε τον δεύτερο αριθμό: "))
	print()
	op=input("Δώσε τον τελεστή [+,-,*,/,//,%] ")
	print()
	if op == "+":
		print(float(a),"KAI",float(b),"ΚΑΝΟΥΝ",a+b)
		print()
	if op == "-":
		print(float(a),"ΠΛΗΝ",float(b),"ΚΑΝΟΥΝ",a-b)
		print()
	if op == "*":
		print(float(a),"ΕΠΙ",float(b),"ΚΑΝΟΥΝ",a*b)
		print()
	if op == "/":
		print(float(a),"ΔΙΑ",float(b),"ΚΑΝΟΥΝ",a/b)
		print()
	if op == "//":
		print("Η ΑΚΕΡΑΙΗ ΔΙΑΙΡΕΣΗ ΤΟΥ",float(a),"ΜΕ ΤΟ",float(b),"ΜΑΣ ΔΙΝΕΙ",a//b)
		print()
	if op == "%":
		print("ΤΟ ΥΠΟΛΟΙΠΟ ΤΗΣ ΔΙΑΙΡΕΣΗ ΤΟΥ",float(b),"ΜΕ ΤΟ",float(b),"ΕΙΝΑΙ",a%b)
		print()
	if op == "ddd":
		print(float(a),"KAI",float(b),"ΚΑΝΟΥΝ",a+b)
		print()
		print(float(a),"ΠΛΗΝ",float(b),"ΚΑΝΟΥΝ",a-b)
		print()
		print(float(a),"ΕΠΙ",float(b),"ΚΑΝΟΥΝ",a*b)
		print()
		print(float(a),"ΔΙΑ",float(b),"ΚΑΝΟΥΝ",a/b)
		print()
		print("Η ΑΚΕΡΑΙΗ ΔΙΑΙΡΕΣΗ ΤΟΥ",float(a),"ΜΕ ΤΟ",float(b),"ΜΑΣ ΔΙΝΕΙ",a//b)
		print()
		print("ΤΟ ΥΠΟΛΟΙΠΟ ΤΗΣ ΔΙΑΙΡΕΣΗ ΤΟΥ",float(b),"ΜΕ ΤΟ",float(b),"ΕΙΝΑΙ",a%b)
		print()
	if op == "end" or op=="END":
		exit()
