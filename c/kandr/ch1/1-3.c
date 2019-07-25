#include <stdio.h>

int main() {
    float fahr, celsius;
    int lower, upper, step;

    lower=0; /* lowerlimitoftemperaturetable*/
    upper=300; /* upperlimit*/
    step=20; /*stepsize*/

    printf("%3s %6s\n", "f", "c");
    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
