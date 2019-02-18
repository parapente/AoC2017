#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int side, num;
    int x, y;
    int place, i;

    scanf("%d", &num);
    side = 1;
    while (num > side*side) {
        side += 2;
    }
    fprintf(stdout, "The number would end up in matrix with a side of %d\n", side);
    place = num-(side-2)*(side-2);
    fprintf(stdout, "place: %d\n", place);

    x=side/2;
    y=-side/2+1;
    for (i=1; i<place && y<side/2; i++) {
	y += 1;
    }
    for (; i<place && x>-side/2; i++) {
	x -= 1;
    }
    for (; i<place && y>-side/2; i++) {
	y -= 1;
    }
    for (; i<place && x<side/2; i++) {
	x += 1;
    }
    fprintf(stdout,"num found at position [%d,%d] - distance:%d\n", x, y, abs(x)+abs(y));
    return 0;
}
