

def clip_with_context(doc, indices, context_size=10):
    """
    Extracts a portion of the document with additional context around it.
    
    Args:
        doc (str): The original document as a string.
        indices (tuple): A tuple containing the start and end indices (start, end).
        context_size (int): Number of characters to include as context on each side.
    
    Returns:
        str: The clipped portion with context.
    """
    start, end = indices
    start = max(0, start - context_size)
    end = min(len(doc), end + context_size)
    return doc[start:end]
