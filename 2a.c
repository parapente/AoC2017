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
    int gotnum, max, min;

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
	max = -1, min = 999999999;
	for (i=0; i<16; i++) {
	    fprintf(stdout, "%d ",nums[i]);
	    if (max < nums[i])
		max = nums[i];
	    if (min > nums[i])
		min = nums[i];
	}
	sum += max-min;
	fprintf(stdout, " --> max: %d, min: %d diff:%d\n", max, min, max-min);
    }

    fprintf(stdout, "checksum: %d\n", sum);

    return 0;
}
