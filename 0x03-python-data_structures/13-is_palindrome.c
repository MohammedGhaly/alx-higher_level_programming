#include "lists.h"
/**
 * is_palindrome - chechks if the linked list is a plindrome or not
 * @head: head node of the linked list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slower = *head, *faster = *head;
	listint_t *previous = NULL, *tmp;

	while (faster != NULL && faster->next != NULL)
	{
		faster = faster->next->next;
		tmp = slower;
		slower = slower->next;
		tmp->next = previous;
		previous = tmp;
	}

	if (faster)
		slower = slower->next;
	while (slower != NULL)
	{
		if (previous->n != slower->n)
			return (0);
		previous = previous->next;
		slower = slower->next;
	}
	return (1);
}
