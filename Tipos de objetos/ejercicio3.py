peso = float(input("Ingrese su peso en kg: "));
Estatura = float(input("Ingrese su estatura: "));

imc = peso//Estatura;
imcre = round(imc, 2);
print("Tu indice de masa corporal es: " + str(imcre));