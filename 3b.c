#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int matrix[1001][1001];
    int side, num, tmp;
    int x, y;
    int place, i, j;

    for (i=0; i<1001; i++)
	for (j=0; j<1001; j++)
	    matrix[i][j] = 0;

    scanf("%d", &num);

    tmp = 1;
    side = 3;
    x = 1001/2;
    y = 1001/2;
    matrix[x][y] = tmp;

    x++;
    while (tmp < num) {
	for (i=0; i<(side-1) && (tmp<num); i++) {
	    tmp = matrix[x-1][y+1] + matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1];
	    matrix[x][y] = tmp;
	    y--;
	}

	y++;
	x--;
	for (i=0; i<(side-1) && (tmp<num); i++) {
	    tmp = matrix[x-1][y+1] + matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1];
	    matrix[x][y] = tmp;
	    x--;
	}

	x++;
	y++;
	for (i=0; i<(side-1) && (tmp<num); i++) {
	    tmp = matrix[x-1][y+1] + matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1];
	    matrix[x][y] = tmp;
	    y++;
	}

	y--;
	x++;
	for (i=0; i<(side-1) && (tmp<num); i++) {
	    tmp = matrix[x-1][y+1] + matrix[x-1][y] + matrix[x-1][y-1] + matrix[x][y-1] + matrix[x+1][y-1] + matrix[x+1][y] + matrix[x+1][y+1] + matrix[x][y+1];
	    matrix[x][y] = tmp;
	    x++;
	}
	side += 2;
    }

    fprintf(stdout, "The first value bigger than %d is %d\n", num, tmp);
    return 0;
}
