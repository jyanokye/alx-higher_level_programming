#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycl
 * @list: list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int	check_cycle(listint_t *list)
{								
	listint_t	*current;
	listint_t	*new;
								
	if(list	==	NULL	||	list->	next	==	NULL)
		return	(0);

	current	=	list->next;
	new	=	list->next->next;

	while(current	&&	new	&&	new->next)
	{

		if(current	==	new)
		{
			return(1);
		}
		current	=	current->next;
		new	=	new->next->next;
	}
	return(0);
}
