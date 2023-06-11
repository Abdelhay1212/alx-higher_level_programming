#include <stdio.h>

/*
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to head of a linked list
 * Return: an integer
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *temp;

	temp = list;
	temp = temp->next->next;
	while (list)
	{
		if (list == temp)
			return (0);
		list = list->next;
		temp = temp->next->next;
	}

	return (1);
}
