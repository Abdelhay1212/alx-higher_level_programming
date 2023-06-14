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
	listint_t *slow = NULL;
	listint_t *temp = malloc(sizeof(listint_t));

	temp->n = number;
	temp->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		temp->next = *head;
		*head = temp;
		return (*head);
	}

	current = (*head)->next;
	slow = *head;

	while (current)
	{
		if (current->n > number)
		{
			temp->next = current;
			slow->next = temp;
			return (*head);
		}
		current = current->next;
		slow = slow->next;
	}

	slow->next = temp;
	return (*head);
}
