algoritmo "calcularMedia"
var
nota1, nota2, nota3, nota4, media: real
nome: caracter
frequencia: inteiro

inicio
escreval ("Digite seu nome:")
leia (nome)

escreval ("Digite sua frequ�ncia:")
leia (frequencia)

escreval ("Digite suas notas")
leia (nota1, nota2, nota3, nota4)

media <- (nota1 + nota2 + nota3 + nota4)/4
se (media >= 7) e (frequencia >= 75) entao
escreval (nome, " Parab�ns voc� foi aprovado, com a m�dia de: ", media)
senao
escreval (nome, " Voc� foi reprovado, sua m�dia foi: ", media, ". J� a sua frequ�ncia foi: ", frequencia)
fimse

fimalgoritmo
