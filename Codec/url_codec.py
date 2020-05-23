import hashlib
class Codec:

    def __init__(self, bucket={}):
        self.bucket = bucket

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while True:
            result = hashlib.sha256(longUrl.encode()).hexdigest()
            shortUrl = result[:7]
            if longUrl not in self.bucket.get(shortUrl):
                self.bucket.put(shortUrl,  longUrl)
                break 
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        try:
            return self.bucket.get(shortUrl)
        except:
            return None