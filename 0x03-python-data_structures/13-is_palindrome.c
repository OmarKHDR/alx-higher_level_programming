#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
listint_t *reverse(listint_t *head);

int is_palindrome(listint_t **head)
{
    listint_t *end = *head;
    listint_t *begin;
    int count = 1, i;

    if ((*head) == NULL )
        return 1;
    if ((*head)->next == NULL)
        return 1;
        // counting nodes
    while (end->next != NULL)
    {
        end = end->next;
        count++;
    }
        // split

    end = *head;
    for (i = 0; i< count / 2; i++)
    {
        end = end->next;
    }

    begin = (count % 2 == 0)? end : end->next ;
    end = *head;

    begin = reverse(begin);

    for (i = 0; i < count / 2; i++)
    {
        if (end->n != begin->n)
            return 0;
        else
        {
            end = end->next;
            begin = begin->next;
        }
    }
    return 1;
}

listint_t *reverse(listint_t *head)
{
    listint_t *nex = NULL, *cur, *prev = NULL;
    cur = head;
    if (cur == NULL)
        return NULL;
    if (cur->next == NULL)
        return cur;
    while (cur != NULL)
    {
        nex = cur->next;
        cur->next = prev;
        prev = cur;
        cur = nex;
    }
    return prev;
}