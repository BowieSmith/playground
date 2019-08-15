#include <stdio.h>

void reverse(char *s);

int main(int argc, char **argv)
{
    size_t size = 1000;
    char str[size];
    char *s = str;
    while (getline(&s, &size, stdin) > 0)
    {
        reverse(s);
        printf("%s\n", s);
    }

}

void reverse(char *s)
{
    int len;
    int i;

    for (i = 0; s[i] != '\0'; i++){}
    len = i;

    for (i = 0; i < len / 2; i++)
    {
        char tmp = s[i];
        s[i] = s[len - i - 1];
        s[len - i - 1] = tmp;
    }
}
