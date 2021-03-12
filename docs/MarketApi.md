# OpenapiClient::MarketApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_spot_market_prices**](MarketApi.md#find_spot_market_prices) | **GET** /market/spot/prices | Get current spot market prices |
| [**find_spot_market_prices_history**](MarketApi.md#find_spot_market_prices_history) | **GET** /market/spot/prices/history | Get spot market prices for a given period of time |


## find_spot_market_prices

> <SpotMarketPricesList> find_spot_market_prices(opts)

Get current spot market prices

Get Equinix Metal current spot market prices.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::MarketApi.new
opts = {
  facility: 'facility_example', # String | Facility to check spot market prices
  plan: 'plan_example' # String | Plan to check spot market prices
}

begin
  # Get current spot market prices
  result = api_instance.find_spot_market_prices(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling MarketApi->find_spot_market_prices: #{e}"
end
```

#### Using the find_spot_market_prices_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotMarketPricesList>, Integer, Hash)> find_spot_market_prices_with_http_info(opts)

```ruby
begin
  # Get current spot market prices
  data, status_code, headers = api_instance.find_spot_market_prices_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotMarketPricesList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling MarketApi->find_spot_market_prices_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **facility** | **String** | Facility to check spot market prices | [optional] |
| **plan** | **String** | Plan to check spot market prices | [optional] |

### Return type

[**SpotMarketPricesList**](SpotMarketPricesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_spot_market_prices_history

> <SpotPricesHistoryReport> find_spot_market_prices_history(facility, plan, from, _until)

Get spot market prices for a given period of time

Get spot market prices for a given plan and facility in a fixed period of time  *Note: In the `200` response, the property `datapoints` contains arrays of `[float, integer]`.*

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::MarketApi.new
facility = 'facility_example' # String | Facility to check spot market prices
plan = 'plan_example' # String | Plan to check spot market prices
from = 'from_example' # String | Timestamp from range
_until = '_until_example' # String | Timestamp to range

begin
  # Get spot market prices for a given period of time
  result = api_instance.find_spot_market_prices_history(facility, plan, from, _until)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling MarketApi->find_spot_market_prices_history: #{e}"
end
```

#### Using the find_spot_market_prices_history_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotPricesHistoryReport>, Integer, Hash)> find_spot_market_prices_history_with_http_info(facility, plan, from, _until)

```ruby
begin
  # Get spot market prices for a given period of time
  data, status_code, headers = api_instance.find_spot_market_prices_history_with_http_info(facility, plan, from, _until)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotPricesHistoryReport>
rescue OpenapiClient::ApiError => e
  puts "Error when calling MarketApi->find_spot_market_prices_history_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **facility** | **String** | Facility to check spot market prices |  |
| **plan** | **String** | Plan to check spot market prices |  |
| **from** | **String** | Timestamp from range |  |
| **_until** | **String** | Timestamp to range |  |

### Return type

[**SpotPricesHistoryReport**](SpotPricesHistoryReport.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

