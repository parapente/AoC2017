#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node {
    int data;
    struct node *next;
} node_t;

void buf_insert(node_t *root, int pos, int data)
{
    int i;
    node_t *tmp, *new_node;

    tmp = root;
    for (i=0; i<(pos-1); i++) {
        tmp = tmp->next;
    }
    new_node = malloc(sizeof(node_t));
    new_node->data = data;
    new_node->next = tmp->next;
    tmp->next = new_node;
}

void print_buf(node_t *node)
{
    do {
        fprintf(stdout, "%d ", node->data);
        node = node->next;
    } while(node!=NULL);
    fprintf(stdout, "\n");
}

int get_data(node_t *node, int pos)
{
    int i = 0;
    do {
        node = node->next;
        i++;
    } while(i<pos);
    return node->data;
}

int main(void)
{
    FILE *fp;
    int i, pos, newpos, len_buf;
    int steps;
    float perc, newperc;
    node_t *root;

    fp = fopen("17.dat", "r");

    if (fp) {
        fscanf(fp, "%d", &steps);
        fprintf(stdout, "%d\n", steps);
        root = malloc(sizeof(node_t));
        root->data = 0;
        root->next = NULL;
        len_buf = 1;
        perc = 0;
        for (i=1; i<50000000; i++) {
            newpos = (steps + pos) % len_buf;
            buf_insert(root, newpos + 1, i);
            len_buf++;
            pos = newpos + 1;
            newperc = 1.0 * i / 50000000 * 100;
            if ((newperc - perc) > 0.01) {
                perc = newperc;
                fprintf(stdout, "%.2f\r", perc);
            }
        }
        fprintf(stdout, "\n%d\n", get_data(root, 1));
    }
    else
	fprintf(stderr, "%s\n", strerror(errno));
    return 0;
}
