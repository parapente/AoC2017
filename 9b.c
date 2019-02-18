#include <stdio.h>
#include <string.h>
#include <errno.h>

int main(void)
{
    FILE *fp;
    int c, garbage, ignore, groups;
    int score;
    int count;
    int garbcount;

    score = 0;
    garbage = ignore = groups = 0;
    count = garbcount = 0;
    fp = fopen("9.dat", "r");

    if (fp) {
	while((c=fgetc(fp)) != '\n') {
	    count++;
	    switch(c) {
		case '<':
		    if (garbage && !ignore)
			garbcount++;
		    if (!ignore)
			garbage = 1;
		    else
			ignore = 0;
		    break;
		case '>':
		    if (!ignore)
			garbage = 0;
		    else
			ignore = 0;
		    break;
		case '!':
		    if (!ignore) {
			if (garbage)
			    ignore = 1;
		    }
		    else
			ignore = 0;
		    break;
		case '{':
		    if (!garbage) {
			groups++;
			score += groups;
			fprintf(stderr,"Group opens at %d, groups: %d, score: %d\n", count, groups, score);
		    }
		    else {
			if (ignore)
			    ignore = 0;
			else
			    garbcount++;
		    }
		    break;
		case '}':
		    if (!garbage) {
			groups--;
			fprintf(stderr,"Group closes at %d, groups: %d\n", count, groups, score);
		    }
		    else {
			if (ignore)
			    ignore = 0;
			else
			    garbcount++;
		    }
		    break;
		default:
		    if (garbage && !ignore)
			garbcount++;
		    if (ignore)
			ignore = 0;
	    }
	}
    }
    else
	fprintf(stderr, "%s\n", strerror(errno));
    fprintf(stdout, "The total score is %d\n", score);
    fprintf(stdout, "I counted %d garbage chars.\n", garbcount);
    return 0;
}
