#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *slower;
	listint_t *faster;

    if (!list)
        return (0);

    slower = list;
    faster = list;

    while (faster && faster->next)
    {
        faster = faster->next->next;
        slower = slower->next;
        if (slower == faster)
            return (1);
    }
    return (0);
}
