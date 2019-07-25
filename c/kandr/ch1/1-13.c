#include <stdio.h>

int main() {
    int word_lengths[50];
    int i, j;
    for (i = 0; i < 50; i++) {
        word_lengths[i] = 0;
    }

    int current_length = 0;
    int c;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (current_length != 0) {
                word_lengths[current_length]++;
                current_length = 0;
            }
        } else {
            current_length++;
        }
    }

    for (i = 0; i < 50; i++) {
        printf("Word size %2d: ", i);
        for (j = 0; j < word_lengths[i]; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
