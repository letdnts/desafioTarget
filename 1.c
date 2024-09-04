#include <stdio.h>

int main(void) {
  int indice = 13;
  int soma = 0;
  int K = 0;

  while (K < indice) {
        K = K + 1; 
        soma = soma + K;
  }
  printf("%d\n", soma);  
  return 0;
}
