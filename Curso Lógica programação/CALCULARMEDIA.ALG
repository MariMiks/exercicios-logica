algoritmo "calcularMedia"
var
nota1, nota2, nota3, nota4, media: real
nome: caracter
frequencia: inteiro

inicio
escreval ("Digite seu nome:")
leia (nome)

escreval ("Digite sua frequência:")
leia (frequencia)

escreval ("Digite suas notas")
leia (nota1, nota2, nota3, nota4)

media <- (nota1 + nota2 + nota3 + nota4)/4
se (media >= 7) e (frequencia >= 75) entao
escreval (nome, " Parabéns você foi aprovado, com a média de: ", media)
senao
escreval (nome, " Você foi reprovado, sua média foi: ", media, ". Já a sua frequência foi: ", frequencia)
fimse

fimalgoritmo
