#include "lists.h"

/**
* check_cycle - Check if a singly linked list has a cycle.
* @list: A pointer to the head of the linked list.
*
* Return: 1 if there is a cycle, 0 if there is no cycle.
*/
int check_cycle(listint_t *list)
{
	listint_t *sharon = list;
	listint_t *philip = list;

	while (sharon != NULL && philip != NULL && philip->next != NULL)
	{
		sharon = sharon->next; /* sharon moved one step */
		philip = philip->next->next; /* philip moved two steps */

		/* If sharon and philip meet, there is a cycle */
		if (sharon == philip)
		{
			return (1); /* Cycle found */
		}
	}

	return (0); /* No cycle found */
}
