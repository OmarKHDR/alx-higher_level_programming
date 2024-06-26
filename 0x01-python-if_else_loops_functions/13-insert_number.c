#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *find = (listint_t *)malloc(sizeof(listint_t));
    listint_t *ptr = *head;

    if (find == NULL)
        return (NULL);
    find->n = number;
    if (ptr == NULL)
        return (find);
    if (ptr->n > find->n)
    {
        find->next = ptr;
        (*head) = find;
        return (find);
    }
    while (ptr->next != NULL && ptr->next->n < find->n)
    {
        ptr = ptr->next;
    }
    find->next = ptr->next;
    ptr->next = find;
    return find;
}
