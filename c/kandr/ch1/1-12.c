#include <stdio.h>

int main() {
    const int OUT = 0;
    const int IN = 1;

    int state = OUT;

    int c;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            state = OUT;
        } else if (state == OUT) {
            putchar('\n');
            putchar(c);
            state = IN;
        } else {
            putchar(c);
        }
    }

    return 0;
}
