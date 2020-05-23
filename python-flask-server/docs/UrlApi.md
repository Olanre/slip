# swagger_client.UrlApi

All URIs are relative to *https://piquednow.swagger.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_url**](UrlApi.md#delete_url) | **DELETE** /url/{tiny_url} | Deletes an encoded url
[**get_all_urls**](UrlApi.md#get_all_urls) | **GET** /url/ | Gets the list of all encoded urls
[**get_long_url_by_id**](UrlApi.md#get_long_url_by_id) | **GET** /url/{tiny_url} | Extract a URL entry by the given tiny URL
[**shrink_url**](UrlApi.md#shrink_url) | **POST** /url/ | Encode a new url

# **delete_url**
> delete_url(tiny_url)

Deletes an encoded url

This will delete a url entry by the given short url as the index

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UrlApi()
tiny_url = 'tiny_url_example' # str | short url to delete

try:
    # Deletes an encoded url
    api_instance.delete_url(tiny_url)
except ApiException as e:
    print("Exception when calling UrlApi->delete_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tiny_url** | **str**| short url to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_urls**
> list[URLs] get_all_urls()

Gets the list of all encoded urls

A list of all tiny: long urls will be retrieved in a key value pair

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UrlApi()

try:
    # Gets the list of all encoded urls
    api_response = api_instance.get_all_urls()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlApi->get_all_urls: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[URLs]**](URLs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_long_url_by_id**
> str get_long_url_by_id(tiny_url)

Extract a URL entry by the given tiny URL

Returns the long url given a short url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UrlApi()
tiny_url = 'tiny_url_example' # str | tiny URL you want to decode

try:
    # Extract a URL entry by the given tiny URL
    api_response = api_instance.get_long_url_by_id(tiny_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlApi->get_long_url_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tiny_url** | **str**| tiny URL you want to decode | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shrink_url**
> URL shrink_url(long_url)

Encode a new url

Converts a long url to a tiny url

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UrlApi()
long_url = 'long_url_example' # str | The long url you wish to convert to a tiny URL

try:
    # Encode a new url
    api_response = api_instance.shrink_url(long_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlApi->shrink_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_url** | **str**| The long url you wish to convert to a tiny URL | 

### Return type

[**URL**](URL.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

