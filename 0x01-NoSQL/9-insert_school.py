def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on provided keyword arguments.
    
    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs representing the fields of the document to be inserted.

    Returns:
        The new document's _id.
    """
    # Insert the document using the keyword arguments
    new_document = mongo_collection.insert_one(kwargs)
    
    # Return the _id of the newly inserted document
    return new_document.inserted_id

