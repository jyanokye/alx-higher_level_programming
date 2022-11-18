#include <stdio.h>
#include <stdlib .h>
#include "lists.h"								

/**
 * print_list - prints all elements of listint_list
 * @h:pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

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
