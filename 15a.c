#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>

void bprint_num(unsigned long long int n) {
    while (n) {
        if (n & 1)
            printf("1");
        else
            printf("0");

        n >>= 1;
    }
    printf("\n");
}

int main(void)
{
    FILE *fp;
    unsigned long long int gena, genb, factora, factorb, match, i;
    unsigned long long int tmpa, tmpb;
    double perc, newperc;

    fp = fopen("15.dat", "r");
    factora = 16807;
    factorb = 48271;
    match = 0;
    perc = 0;

    if (fp) {
        fscanf(fp, "%llu,%llu", &gena, &genb);
        fprintf(stdout, "Read %llu %llu\n", gena, genb);
        fprintf(stdout, "%.2lf%%\r", perc);
        for (i=0; i<40000000; i++) {
            gena = gena * factora;
            gena = gena % 0x7fffffffULL;
            genb = genb * factorb;
            genb = genb % 0x7fffffffULL;
            tmpa = gena & 0xffffULL;
            tmpb = genb & 0xffffULL;
            /* bprint_num(gena); */
            /* bprint_num(genb); */
            /* printf("\n"); */
            if (tmpa == tmpb) {
                //printf("Match: %llu %llu %llu %llu\n", gena, genb, tmpa, tmpb);
                match++;
            }
            newperc = (1.0 * i / 40000000) * 100;
            if ((newperc - perc) > 0.01) {
                perc = newperc;
                fprintf(stdout, "%.2lf%%\r", newperc);
                fflush(stdout);
            }
        }
    }
    else
	fprintf(stderr, "%s\n", strerror(errno));
    fprintf(stdout, "\nMatch: %llu", match);
    return 0;
}
