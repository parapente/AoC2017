#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    char row[100000];
    char num[10];
    int nums[16];
    int sum, i, j, k, tmpnum;
    int gotnum, a, b, rowdiv;

    sum = 0;
    while(fgets(row,100000,stdin)!=NULL) {
	i = 0;
	j = 0;
	k = 0;
	gotnum = 0;
	while(row[i]!='\n') {
	    if (isdigit(row[i])) {
		num[j] = row[i];
		j++;
		gotnum = 1;
	    }
	    else {
		if (gotnum) {
		    num[j] = '\0';
		    nums[k] = atoi(num);
		    j = 0;
		    k++;
		    gotnum = 0;
		}
	    }
	    i++;
	}
	if (gotnum) {
	    num[j] = '\0';
	    nums[k] = atoi(num);
	}

	for (i=0; i<16; i++) {
	    fprintf(stdout, "%d ",nums[i]);
	}

	for (i=0; i<15; i++) {
	    for (j=i+1;j<16;j++) {
		if (nums[i]<nums[j]) {
		    a = nums[j];
		    b = nums[i];
		}
		else {
		    a = nums[i];
		    b = nums[j];
		}
		if ((a % b) == 0) {
		    rowdiv = a / b;
		    fprintf(stdout, " --> a: %d, b: %d div:%d\n", a, b, rowdiv);
		    sum += rowdiv;
		}
	    }
	}
    }

    fprintf(stdout, "checksum: %d\n", sum);

    return 0;
}
