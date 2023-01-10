#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * palindrome_check - checks if the list is palindrome
 * using recursion
 * @l: left most node
 * @r: right most node
 *
 * Return: 1 if palindrome (success) 0 if it is not
 */
int palindrome_check(listint_t **l, listint_t *r)
{
	int resultlist;

	if (r == NULL) /* Base case */
		return (1);

	/* Check if the sub-list is a palindrome */
	resultlist = palindrome_check(l, r->next);
	if (resultlist == 0) /* No need to check then */
		return (0);

	resultlist = (r->n == (*l)->n);
	*l = (*l)->next;
	return (resultlist);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if palindrome, 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	/* An empty list is considered a palindrome */
	if (head == NULL)
		return (1);
	return (palindrome_check(head, *head));
}
