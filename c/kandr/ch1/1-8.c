#include <stdio.h>

int main() {
    int bc = 0;     // blank count
    int tc = 0;     // tab count
    int nc = 0;     // newline count

    printf("Enter any characters\n");
    printf("Use cntl-d to end input with EOF\n");

    int c;
    while ((c = getchar()) != EOF) {
        if (c == ' ')
            ++bc;
        else if (c == '\t')
            ++tc;
        else if (c == '\n')
            ++nc;
    }

    printf("Blanks: %d, Tabs: %d, Newlines: %d\n", bc, tc, nc);

    return 0;
}
