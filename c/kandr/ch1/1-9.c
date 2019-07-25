#include <stdio.h>

int main() {
    int c;
    int last_char = 0;

    while ((c = getchar()) != EOF) {
        if (c != ' ')
            putchar(c);
        else
            if (last_char != ' ')
                putchar(c);
        last_char = c;
    }
}
