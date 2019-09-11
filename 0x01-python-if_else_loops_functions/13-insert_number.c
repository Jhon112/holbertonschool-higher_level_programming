#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - adds a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in list
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *next_node;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if ((current->next == NULL) && (current->n < new->n))
                        {
                                current->next = new;
                                break;
                        }
			if (current->n > new->n)
			{
				new->next = current;
				*head = new;
				break;
			}
			next_node = current->next;
			if (next_node->n > new->n)
			{
				new->next = current->next;
				current->next = new;
				break;
			}
			current = current->next;
		}
	}
	return (new);
}
