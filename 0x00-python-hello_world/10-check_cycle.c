#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"



int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *check ;
	int counter = 0,i;
	while(current != NULL)
	{
		current = current->next;
		counter ++;

		if (current == NULL)
			return (0);
		for (i=0; i<counter; i++)
		{
			check = list;
			if (check == current)
				return (1);
			check = check->next;
		}
	}
	return (0);
}