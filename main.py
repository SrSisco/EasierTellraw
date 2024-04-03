raw_input = input("Cadena principal: ")
raw_text_identifier = input("i_txt: ")
raw_times_identifier = input("i_num: ")
offset = int(input("Offset:"))
text = input("Pon el texto: ")
result = input("Nombre del txt donde estará la salida: ")
index = 0 + offset
finale = ""
with open(result+".txt", "w") as f:
    for x in text:
        finale = finale.__add__(x)
        a = raw_input.replace(raw_text_identifier, finale)
        a = a.replace(raw_times_identifier, str(index))
        if(x != " "):
            index += 1
            f.write(a + "\n")

print("Por SrSisco uwu (reinicia el programa para la siguiente cadena)")
