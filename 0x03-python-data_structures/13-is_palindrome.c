#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int length = 0, i = 0;
	listint_t *temp = NULL;

	if (head == NULL)
		return (0);

	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		length++;
	}

	int arr[length];

	temp = *head;
	while (temp != NULL)
	{
		arr[--length] = temp->n;
		temp = temp->next;
	}

	temp = *head;
	while (temp != NULL)
	{
		if (temp->n != arr[i])
			return (0);
		temp = temp->next;
		i++;
	}
	return (1);
}
