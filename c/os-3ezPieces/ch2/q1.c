#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char** argv) {
    int x = 100;
    int rc = fork();
    if (rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        x = 200;
        printf("Hello from child. PID: %d. x = %d.\n", getpid(), x);
    } else {
        x = 300;
        printf("Hello from parent. PID: %d. x = %d.\n", getpid(), x);
    }
}
