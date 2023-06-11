#include <stdio.h>
#include "lists.h"

/*
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to head of a linked list
 * Return: an integer
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (0);
	}

	return (1);
}
