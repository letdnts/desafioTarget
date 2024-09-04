#include <stdio.h>

int pertence_fib(int num) {
    if (num < 0) return 0;  

    int a = 0, b = 1, c = 0;

    if (num == a || num == b) return 1;  

    while (c < num) {
        c = a + b;  
        a = b;
        b = c;
    }
    return c == num;  
}

int main(void) {
    int num;
    printf("Informe um número: ");
    scanf("%d", &num);

    if (pertence_fib(num)) {
        printf("O número %d pertence à sequência de Fibonacci.\n", num);
    } else {
        printf("O número %d não pertence à sequência de Fibonacci.\n", num);
    }

    return 0;
}