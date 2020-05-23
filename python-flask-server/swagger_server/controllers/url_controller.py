import connexion
import six

from swagger_server.models.url import URL  # noqa: E501
from swagger_server.models.ur_ls import URLs  # noqa: E501
from swagger_server import util
from drivers.Cache import RedisCache
from Codec.url_codec import Codec

def if __name__ == "__main__":
    main()

def main():
    cache = RedisCache()
    codec = Codec(cache)

def delete_url(tiny_url):  # noqa: E501
    """Deletes an encoded url

    This will delete a url entry by the given short url as the index # noqa: E501

    :param tiny_url: short url to delete
    :type tiny_url: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_urls():  # noqa: E501
    """Gets the list of all encoded urls

    A list of all tiny: long urls will be retrieved in a key value pair # noqa: E501


    :rtype: List[URLs]
    """
    return 'do some magic!'


def get_long_url_by_id(tiny_url):  # noqa: E501
    """Extract a URL entry by the given tiny URL

    Returns the long url given a short url # noqa: E501

    :param tiny_url: tiny URL you want to decode
    :type tiny_url: str

    :rtype: str
    """
    return 'do some magic!'


def shrink_url(long_url):  # noqa: E501
    """Encode a new url

    Converts a long url to a tiny url # noqa: E501

    :param long_url: The long url you wish to convert to a tiny URL
    :type long_url: str

    :rtype: URL
    """
    
    return 'do some magic!'
