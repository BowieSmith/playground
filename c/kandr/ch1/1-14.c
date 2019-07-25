#include <stdio.h>

int main() {
    int ascii_chars[128];
    int i, j, c;

    for (i = 0; i < 128; i++) {
        ascii_chars[i] = 0;
    }

    while ((c = getchar()) != EOF) {
        ascii_chars[c]++;
    }

    for (i = 0; i < 128; i++) {
        printf("%c : ", i);
        for (j = 0; j < ascii_chars[i]; j++) {
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}
