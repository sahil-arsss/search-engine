from preprocessing.processor import preprocess_text


def process_query(query):
    """
    Convert raw query → tokens
    """
    return preprocess_text(query)


def search(query, index):
    """
    Basic search:
    - AND logic (all words must match)
    """
    tokens = process_query(query)

    if not tokens:
        return []

    # Get document sets for each token
    doc_sets = []

    for token in tokens:
        if token in index:
            doc_sets.append(index[token])
        else:
            # If any word not found → no result (AND logic)
            return []

    # Intersection of all sets (AND search)
    result_docs = set.intersection(*doc_sets)

    return list(result_docs)