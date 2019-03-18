def top_n(items,n):
    """Return the top n items in an array in descending order.
    Args:
        items(array): list or array-like object containing numerical values.
        n (int): number of top items to return.
    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8,3,2,7,4],3)
        [8,7,3]

    """
    for a in range(n): #keep sorting until we have the top n items
        for b in range(len(items)-1-a):
            if items[b] > items[b+1] : #if this item is bigger than next item..
                items[b], items[b+1] = items[b+1], items[b] #swap the two!

    #get last two items
    top_n = items[-n:]

    return in descending order
    return top_n[::-1]
