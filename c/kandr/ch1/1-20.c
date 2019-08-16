#include <stdio.h>
#include <stdlib.h>

#define DEFAULT_TAB_SPACE 4

int main(int argc, char *argv[])
{
    const char usage[] = "Usage: detab [tab_width]";
    long tab_width;

    if (argc < 2)
    {
        tab_width = DEFAULT_TAB_SPACE;
    }
    else
    {
        tab_width = strtol(argv[1], NULL, 10);
        if (tab_width == 0)
        {
            printf("%s\n", usage);
            return(0);
        }
    } 

    char c;
    int i = 0;
    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
        {
            i = 0;
            putchar(c);
        }
        else if (c != '\t')
        {
            i++;
            putchar(c);
        }
        else
        {
            int total_spaces = tab_width - (i % tab_width);
            for (int j = 0; j < total_spaces; j++)
            {
                putchar(' ');
                i++;
            }
        }
    }
}

