Algoritmo "reajusteSalarial"
//Escreva um algoritmo para calcular o reajuste salarial e imprimir o sal�rio
//reajustado.
//a) 25% para aqueles que ganham at� 1 m�nimo
//b) 50% para aqueles que ganham at� 3 sal�rios m�nimos
//c) 10% para aqueles que ganham acima de 3 sal�rios m�nimos
var
salario, salarioReajustado, salarioMinimo: real

inicio
escreval ("Entre com o sal�rio atual")
leia (salario)
escreval ("Entre com o sal�rio minimo")
leia (salarioMinimo)

se (salario <= salarioMinimo) entao
   salarioReajustado <- salario*1.25
   senao
        se (salario >= salarioMinimo) entao
        salarioReajustado <- salario*1.50
   senao
     salarioREajustado <- salario*1.10
     fimse
fimse
escreval ("Sal�rio reajustado: R$ ", salarioReajustado)

Fimalgoritmo