#include "lists.h"
/**
 * get_length - returns length of list
 * @head: pointer to first node
 *
 * Return: length of list
 */
int get_length(listint_t *head)
{
	int length = 0;

	while (head != NULL)
	{
		length++;
		head = head->next;
	}
	return (length);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of head of list
 *
 * Return: 0 if not palindrome, 1 if it's
 */
int is_palindrome(listint_t **head)
{
	int length, i, j;
	listint_t *current = *head, *half = *head;

	length = get_length(*head);
	if (length == 1)
		return (1);

	i = 0;
	while (i < length / 2)
	{
		half = half->next;
		i++;
	}
	if (length % 2 == 0)
		i--;
	while (half != NULL)
	{
		current = *head;
		j = i;
		while (j > 0)
		{
			current = current->next;
			j--;
		}
		if (half->n == current->n)
		{
			half = half->next;
			i--;
			continue;
		}
		return (0);
	}
	return (1);
}
