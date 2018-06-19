

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(1, len(meals)):
        if(meals[i] == meals[i-1]):
            return True

    return False

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    return [x > thresh for x in L]

def slots_survival_probability(start_balance, n_spins, n_simulations):
    """Return the approximate probability (as a number between 0 and 1) that we can complete the 
    given number of spins of the slot machine before running out of money, assuming we start 
    with the given balance. Estimate the probability by running the scenario the specified number of times.
    
    >>> slots_survival_probability(10.00, 10, 1000)
    1.0
    >>> slots_survival_probability(1.00, 2, 1000)
    .25
    """
    pass

def count_negatives(nums):
    nums.append(0)
    # We could also have used the list.sort() method, which modifies a list, putting it in sorted order.
    nums = sorted(nums)
    return nums.index(0)

if __name__ == '__main__':

    # build elementwise list
    l = [1, 2, 3, 4]
    threshold = 2
    res = elementwise_greater_than(l, threshold)
    print(res)