# metal.CapacityApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_capacity_for_facility**](CapacityApi.md#check_capacity_for_facility) | **POST** /capacity | Check capacity
[**find_capacity_for_facility**](CapacityApi.md#find_capacity_for_facility) | **GET** /capacity | View capacity


# **check_capacity_for_facility**
> CapacityCheckPerFacilityList check_capacity_for_facility(facility)

Check capacity

Validates if a deploy can be fulfilled.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.CapacityApi(api_client)
    facility = metal.CapacityInput() # CapacityInput | Facility to check capacity in

    try:
        # Check capacity
        api_response = api_instance.check_capacity_for_facility(facility)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapacityApi->check_capacity_for_facility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facility** | [**CapacityInput**](CapacityInput.md)| Facility to check capacity in | 

### Return type

[**CapacityCheckPerFacilityList**](CapacityCheckPerFacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_capacity_for_facility**
> CapacityList find_capacity_for_facility()

View capacity

Returns a list of facilities and plans with their current capacity.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.CapacityApi(api_client)
    
    try:
        # View capacity
        api_response = api_instance.find_capacity_for_facility()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CapacityApi->find_capacity_for_facility: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CapacityList**](CapacityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

