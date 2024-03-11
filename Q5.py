texto = "abcde"
ind = -1
new_texto = ""
for letra in texto:
    new_texto = new_texto + texto[ind]
    ind = ind - 1
print(new_texto)