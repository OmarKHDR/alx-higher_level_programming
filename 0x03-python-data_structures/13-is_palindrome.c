#include <stdio.h>
#include <stdlib.h>
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
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

    begin = end->next ;
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