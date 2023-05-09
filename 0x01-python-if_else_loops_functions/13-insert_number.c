#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a node anywhere in a linked list
 * @head: head node of the list
 * @number: number of the new node
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
        if (!new)
                return (NULL);
        new->n = number;
	if (head == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	if ((*head)->n > number)
	{
		temp = *head;
		*head = new;
		new->next = temp;

		head = &new;
		return (*head);
	}

	temp = *head;
	while (temp->next != NULL && temp->next->n < number)
		temp = temp->next;

	new->next = temp->next;
	temp->next = new;
	temp->next = new;
	return (new);
}
