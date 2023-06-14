#include "lists.h"
#include <stdlib.h>

/*
 * insert_node - insert a node in a linked list
 * @head: linked list to insert in
 * @number: number to insert in the linked list
 * Return: void
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *temp = NULL;

	current = *head;
	while (current)
	{
		if (current->n <= number)
			current = current->next;
		if (current->n > number)
		{
			temp->n = number;
			temp->next = current->next;
			current = temp;
			return (0);
		}
	}
}
