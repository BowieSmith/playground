#include <stdio.h>

int main() {
    float fahr, celsius;
    int lower, upper, step;

    lower=0; /* lowerlimitoftemperaturetable*/
    upper=100; /* upperlimit*/
    step=10; /*stepsize*/

    printf("%3s %6s\n", "c", "f");
    celsius = lower;
    while (celsius <= upper) {
        fahr = (9.0 / 5.0) * celsius + 32.0;
        printf("%3.0f %6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
}
