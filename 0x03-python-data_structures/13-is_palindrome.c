#include "lists.h"

/*
 * is_palindrome - checks a linked list if it is a palindrome
 * @head: linked list to check if it is a palindrome
 * Retrun: integer
 */
int is_palindrome(listint_t **head)
{
	int length = 0, i = 0;
	listint_t *temp = NULL;

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
