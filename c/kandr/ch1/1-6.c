#include <stdio.h>

int main() {
    printf("Enter a letter\n");
    printf("Press cntl-d to enter EOF value\n");
    printf("getchar() != EOF: %d\n", getchar() != EOF);
    return 0;
}
