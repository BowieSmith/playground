#include <unistd.h>
#include <fcntl.h>

int main(int argc, char** argv) {
    int fd = open("./q2_stuff", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
    int rc = fork();
    if (rc < 0) {
        fprintf(stderr, "Fork failed\n");
    } else if (rc == 0) {
        printf("In child. Adding 100 - 199 to q2_stuff");
        
    } else {
        printf("In parent. Adding 0 - 99 to q2_stuff");
    }
}
