// Testing strncat

#include <stdio.h>
#include <string.h>

int main()
{
    char buffer[BUFSIZ] = {0};
    char *path = "this/is/a/path";
    char *dir = "/data/dir/";

    strncpy(buffer, dir, BUFSIZ);
    strncat(buffer, path, BUFSIZ);

    printf("%s\n", buffer);
}
