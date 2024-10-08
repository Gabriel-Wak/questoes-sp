# Defina a string a ser invertida
string_original = input("Digite uma string: ")

# Crie uma string vazia para armazenar a string invertida
string_invertida = ""

# Itere sobre a string original de trás para frente
for i in range(len(string_original) - 1, -1, -1):
    # Adicione cada caractere à string invertida
    string_invertida += string_original[i]

# Imprima a string invertida
print("String invertida:", string_invertida)