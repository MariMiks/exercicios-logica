Algoritmo "matrizes"
//matrizes
// M -> linha
// N -> coluna
// comando sempre será MxN
var
matrizes: vetor [1..2, 1..2] de inteiro
linha, coluna: inteiro

inicio
para linha de 1 ate 2 faca
       para coluna de 1 ate 2 faca
       escreval ("Digite um valor para a posição [", linha, ",", coluna, "]:")
       leia (matrizes[linha, coluna])
       fimpara
escreval
fimpara

escreval ("-----------------------")

para linha de 1 ate 2 faca
       para coluna de 1 ate 2 faca
       escreva (matrizes[linha, coluna])
       fimpara
escreval
fimpara

Fimalgoritmo