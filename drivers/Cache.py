import abc
class Cache:
    """
    This cache allows us to abstract in memory DB access
    c = Cache
    c.put("a", 1)
    c.get("a") # returns '1'
    c.put("b","two")
    c.get("b") #returns 2

    This requires redis to work
    """

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'put') and 
                callable(subclass.put) and 
                hasattr(subclass, 'get') and 
                callable(subclass.get) and
                hasattr(subclass, 'remove') and 
                callable(subclass.remove) and
                hasattr(subclass, 'clear') and 
                callable(subclass.clear))

    @abc.abstractmethod
    def put(self, key, value):
        """
        inserts a new  object into the cache defined by the key and value
        input:
        key: The key for the cache object to be insert
        value: The value pointed to by the key
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, key):
        """
        gets the object from the cache indexed by the key
        input:
            key: The key for the cache object to retrieved
        """
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, key):
        """
        Remove the object indexed by the key from the cache 
        input
            key: The key for the cache object to be removed

        """
        raise NotImplementedError
    
    @abc.abstractmethod
    def clear(self):
        """
        Deletes all the objects in the cache
        """
        raise NotImplementedError 