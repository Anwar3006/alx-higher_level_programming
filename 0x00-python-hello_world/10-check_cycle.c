#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *c1, *c2;

	if (list == NULL || list->next == NULL)
		return (0);

	c1 = list->next;
	c2 = list->next->next;

	while (c1 && c2 && c2->next)
	{
		if (c1 == c2)
			return (1);

		c1 = c1->next;
		c2 = c2->next->next;
	}

	return (0);
}