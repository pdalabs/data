#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *link;
};


struct node *first = NULL, *head, *ptr, *temp, *temp1;

void create() {
    if (first != NULL) {
        printf("\nLinkedList already created.");
        return;
    }

    head = (struct node*)malloc(sizeof(struct node));
    printf("\nEnter value for head node : ");
    scanf("%d", &head->data);

    head->link = NULL;
    first = head;
}
void insert_beg() {
    ptr = (struct node*)malloc(sizeof(struct node));
    printf("\nEnter the data for the new node : ");
    scanf("%d", &ptr->data);
    ptr->link = first;
    first = ptr;
}
void insert_end() {
    temp = (struct node*)malloc(sizeof(struct node));
    printf("\nEnter the data for the new node : ");
    scanf("%d", &temp->data);
    temp->link = NULL;
    if (first == NULL) {
        first = temp;
        return;
    }
    ptr = first;
    while (ptr->link != NULL) {
        ptr = ptr->link;
    }
    ptr->link = temp;
}
void del_beg() {
    if (first == NULL) {
        printf("\nLinked List is already empty.");        
    }
    else {
        temp = first;
        first = first->link;
        free(temp);
    }
}
void del_end() {
    if (first == NULL) {
        printf("\nLinked List is already empty.");
    }
    else if (first->link == NULL) {
        free(first);
        first = NULL;
    }
    else {
        temp = first;
        temp1 = first;
        while (temp->link != NULL) {
            temp1 = temp;
            temp = temp->link;
        }
        temp1->link = NULL;
        free(temp);
        temp = NULL;
    }
}
void display() {
    if (first == NULL) {
        printf("\nThe Linked List is already empty.");
        return;
    }
    head = first;
    printf("\nThe Linked List is  : ");
    while (head != NULL) {
        printf("%d \t", head->data);
        head = head->link;
    }  
}

int main()
{
    int ch;

    printf("\n\n Singly linked lidt");
    printf("\n\n 1.CREATE");
        printf("\n 2.INSERT BEGINING NODE");
        printf("\n 3.INSERT ENDING NODE");
        printf("\n 4.DELETE BEGINING NODE");
        printf("\n 5.DELETE END NODE");
        printf("\n 6.EXIT");
    while (1)
    {
        printf("\n\n Enter your choice:");
        scanf("%d", &ch);

        switch (ch)
        {
            case 1:
                create();
                display();
                break;

            case 2:
                insert_beg();
                display();
                break;

            case 3:
                insert_end();
                display();
                break;

            case 4:
                del_beg();
                display();
                break;

            case 5:
                del_end();
                display();
                break;

            case 6:
                exit(0);

            default:
                printf("Invalid choice...");
        }
    }
}


