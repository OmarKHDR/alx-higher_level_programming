#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list ;

	while (first != NULL && second != NULL)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}