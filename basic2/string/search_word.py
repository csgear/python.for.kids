

def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents
    containing the keyword.
    """

    indices = []

    for i, s in enumerate(doc_list):
        tokens = s.split()
        normalized = [token.rstrip(',.').lower() for token in tokens]
        # print(normalized)
        if (keyword.lower() in normalized):
            indices.append(i)

    return indices

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    indices = {} 

    for keyword in keywords:
        indices[keyword] = word_search(doc_list, keyword)
    
    return indices


def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    s = '' 
    l, r = '/', '\\'
    middle = height // 2

    for row in range(height):
        if row == middle:
            l, r = r, l
        
        if row < middle:
            nchars = row + 1
        else:
            nchars = height - row
        
        left = (l * nchars).rjust(middle)
        right = (r * nchars).ljust(middle)
        s += left + right + '\n'

    return s



def conditional_roulette_probs(history):
    """
    Example: 
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5}, 
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """
    counts = {}

    for i in range(1, len(history)):
        roul, prev = history[i], history[i-1]
        if prev not in counts:
            counts[prev] = {}
        if roul not in counts[prev]:
            counts[prev][roul] = 0
        counts[prev][roul] += 1

    probs = {}

    for prev, nexts in counts.items():
        total = sum(nexts.values())
        sub_probs = {next_spin : next_count / total for next_spin, next_count in nexts.items()}
        probs[prev] = sub_probs
    
    return probs

if __name__ == '__main__':
    # single keyword 
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    keyword = 'casino'
    indices = word_search(doc_list, keyword)
    print(indices)

    # check multi indices
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    keywords = ['casino', 'they']
    indices = multi_word_search(doc_list, keywords)
    print(indices)

    # conditional probs
    history = [1, 3, 1, 5, 1]
    probs = conditional_roulette_probs(history)
    print(probs)

    # print great diamond
    height = 10
    s = diamond(height)
    print(s)