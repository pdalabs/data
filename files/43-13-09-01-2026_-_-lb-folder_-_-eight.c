#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *next;
};

int main() {

    int item, n;
    struct node *head;
    struct node *temp;
    struct node *tail;
    struct node *prev;
    struct node *curr;
    struct node *next;

    temp = (struct node*)malloc(sizeof(struct node));
    head = temp;

    printf("\nEnter the size of the linked list : ");
    scanf("%d", &n);

    printf("\nEnter the linked list to be reversed : ");
    temp = (struct node*)malloc(sizeof(struct node));
    scanf("%d", &item);
    temp->value = item;
    head = temp;
    n--;
    while (n != 0) {
        temp->next = (struct node*)malloc(sizeof(struct node));
        temp = temp->next;
        scanf("%d", &item);
        temp->value = item;
        --n;
    }
    temp->next = NULL;
    tail = temp;
    temp = head;

    printf("\nReversing the Linked List.");
    prev = NULL;
    curr = next = head;
    while ( curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    temp = tail;
    while (temp) {
        printf("%d\t", temp->value);
        temp = temp->next;
    }
    return 0;
}