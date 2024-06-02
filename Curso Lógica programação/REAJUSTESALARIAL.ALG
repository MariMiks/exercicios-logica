Algoritmo "reajusteSalarial"
//Escreva um algoritmo para calcular o reajuste salarial e imprimir o salário
//reajustado.
//a) 25% para aqueles que ganham até 1 mínimo
//b) 50% para aqueles que ganham até 3 salários mínimos
//c) 10% para aqueles que ganham acima de 3 salários mínimos
var
salario, salarioReajustado, salarioMinimo: real

inicio
escreval ("Entre com o salário atual")
leia (salario)
escreval ("Entre com o salário minimo")
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
escreval ("Salário reajustado: R$ ", salarioReajustado)

Fimalgoritmo