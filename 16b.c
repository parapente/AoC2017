#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    FILE *fp;
    char *prog, *token, *a, *b, tmp;
    char buf[1000000], buf_sav[1000000], t1[17], t2[17];
    int i;
    int spin;
    double perc, newperc;

    fp = fopen("16.dat", "r");

    if (fp) {
        prog = malloc(17);
        for (i=0; i<16; i++)
            prog[i] = 'a' + i;
        prog[16] = '\0';

        fprintf(stdout, "Starting pos: %s\n", prog);
        fgets(buf, 1000000, fp);
        buf[strlen(buf)-1] = '\0'; // Remove '\n'
        strcpy(buf_sav, buf);
        /* fprintf(stdout,"Starting buf: %s\n", buf); */
        perc = 0;
        for (i=0; i<1000000000; i++) {
        /* for (i=0; i<1; i++) { */
            strcpy(buf, buf_sav);
            token = strtok(buf, ",");
            while(token != NULL) {
                if (token[0]=='s') {
                    // Spin
                    memset(t1, '\0', sizeof(t1));
                    memset(t2, '\0', sizeof(t2));
                    spin = atoi(token + 1);
                    strcpy(t1, prog + 16 - spin);
                    strncpy(t2, prog, 16 - spin);
                    strcpy(prog, t1);
                    strcat(prog, t2);
                }
                else if (token[0]=='x') {
                    // eXchange
                    memset(t1, '\0', sizeof(t1));
                    memset(t2, '\0', sizeof(t2));
                    if (token[2]=='/') {
                        strncpy(t1, token + 1, 1);
                        strcpy(t2, token + 3);
                    }
                    else {
                        strncpy(t1, token + 1, 2);
                        strcpy(t2, token + 4);
                    }
                    tmp = prog[atoi(t1)];
                    prog[atoi(t1)] = prog[atoi(t2)];
                    prog[atoi(t2)] = tmp;
                }
                else if (token[0]=='p') {
                    // Partner
                    a = strchr(prog, token[1]);
                    b = strchr(prog, token[3]);
                    tmp = a[0];
                    a[0] = b[0];
                    b[0] = tmp;
                }
                else {
                    fprintf(stdout, "Ooops! Found %s...", token);
                    exit(1);
                }
                //fprintf(stdout, "Token: %s - %s\n", token, prog);
                //getchar();
                newperc = 1.0 * i / 1000000000 * 100;
                if ((newperc - perc) > 0.01) {
                    perc = newperc;
                    fprintf(stdout, "%.2f\r", perc);
                    fflush(stdout);
                }
                token = strtok(NULL, ",");
            }
            fprintf(stdout, "\nProgs: %s\n", prog);
        }
    }
    else
	fprintf(stderr, "%s\n", strerror(errno));
    fprintf(stdout, "\nProgs: %s\n", prog);
    return 0;
}
