from redis import Redis
class RedisCache(object):
    """
    This cach allows us to abstract the driver for Redis
    r = RedisCache
    r.put("a", 1)
    r.get("a") # returns '1'
    r.put("b","two")
    r.get("b") #returns 2

    This requires redis to work
    """

    def __init__(self, host = "localhost", port=6379, db=0):
        """
        Initialize a database defined by the connection provided

        Input:
            host: the host to connect to the redis server, default is localhost
            port: The port number to connect on, default is 6379
            db: the redis database, default is 0
        """
        self._redis = Redis(host, port, db)

    def put(self, key, value, expiration_time=3600):
         """
        inserts a new  object into the cache defined by the key and value
        input:
            key: The key for the cache object to be insert
            value: The value pointed to by the key
            expiration_time: The time to wait until the object is removed from the cache which defaults to 3600 seconds.
        Raises: 
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.
        """
        self.redis.setex(key, value, expiration_time)

    def get(self, key):
        """
        gets the object from the cache indexed by the key
        input:
            key: The key for the cache object to retrieved
        Raises: 
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.
        """
        return self.redis.get(key)

    def remove(self, key):
        """
        Remove the object indexed by the key from the cache 
        input
            key: The key for the cache object to be removed

        Raises:
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.

        """
        return self.redis.lpop(key)
    
    def clear(self):
        """
        Deletes all the objects in the cache

        Raises:
            redis.exceptions.ConnectionError: An error if there is some problem on the connection
                with Redis server.

        """
        self.redis.flushdb()