#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char captcha[10000];
    int sum, i, clen, mid;
    char prev,first;

    sum = 0;
    if (fgets(captcha, 10000, stdin) == NULL) {
	fprintf(stdout, "An error has occured!\n");
    }
    else {
	prev = '-';
	first = captcha[0];
	fprintf(stdout, "captcha: %s\n", captcha);
	clen = strlen(captcha) - 1;
	mid = clen / 2;
	for (i=0; i<clen; i++) {
	    fprintf(stdout, "i=%d, captcha[i]='%c'\n", i, captcha[i]);
	    if (captcha[i] == captcha[(i+mid)%clen]) {
		fprintf(stdout, "Found one!\n");
		sum += captcha[i]-'0';
	    }
	    prev = captcha[i];
	}
	fprintf(stdout, "The sum is %d.\n", sum);
    }

    return 0;
}
