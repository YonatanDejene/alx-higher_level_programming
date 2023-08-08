#include "lists.h"

/**
 * check_cycle - check wheather a linked list contain cycle
 * @list: the linked list to be checked
 *
 * Return: if the list has a cycle 1, if not 0
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *s = list;

	if(!list)
		return (0);

	while (s && f && f->next)
	{
		s = s_>next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}
