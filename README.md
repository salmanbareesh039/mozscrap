# Moz DA PA Metrics

This Apify actor fetches Moz Domain Authority (DA) and Page Authority (PA) metrics for any given domain using the Seomator API.

## Features

- Fetches Domain Authority and Page Authority scores
- Retrieves spam score and link propensity data
- Provides comprehensive backlink metrics including:
  - Total pages linking to subdomain
  - External pages linking to subdomain
  - Root domains linking to subdomain
  - NoFollow and redirect page counts
  - Deleted page metrics

## Input

The actor expects a JSON input with the following structure:

```json
{
    "domain": "example.com"
}
```

### Input Parameters

- **domain** (required): The domain name to analyze (e.g., "example.com")

## Output

The actor returns a JSON object with the following metrics:

```json
{
    "domain": "example.com",
    "error": "",
    "domain_authority": 85,
    "page_rank": 7.2,
    "spam_score": 2,
    "link_propensity": 4.5,
    "total_pages": 12500,
    "external_pages": 8500,
    "root_domains": 1250,
    "nofollow_pages": 850,
    "redirect_pages": 150,
    "deleted_pages": 25,
    "external_nofollow_pages": 450,
    "external_redirect_pages": 75,
    "nofollow_root_domains": 125
}
```

### Output Fields

- **domain**: The analyzed domain
- **error**: Error message if any issues occurred
- **domain_authority**: Moz Domain Authority score (0-100)
- **page_rank**: Page rank value
- **spam_score**: Moz spam score (0-17, lower is better)
- **link_propensity**: Link building difficulty score
- **total_pages**: Total pages linking to the subdomain
- **external_pages**: External pages linking to the subdomain
- **root_domains**: Number of root domains linking to the subdomain
- **nofollow_pages**: Pages with nofollow links to the subdomain
- **redirect_pages**: Redirect pages linking to the subdomain
- **deleted_pages**: Deleted pages that previously linked to the subdomain
- **external_nofollow_pages**: External pages with nofollow links
- **external_redirect_pages**: External redirect pages
- **nofollow_root_domains**: Root domains with nofollow links

## Usage

1. Go to the [Apify Console](https://console.apify.com/actors)
2. Search for "Moz DA PA Metrics" or use this actor
3. Click "Try for free"
4. Enter the domain you want to analyze
5. Click "Start" to run the actor
6. View the results in the "Results" tab

## Error Handling

The actor includes comprehensive error handling:
- Returns error messages for invalid domains
- Handles API timeouts and network issues
- Validates response data before processing

## API Rate Limits

This actor uses the Seomator API endpoint. Please be mindful of rate limits when running multiple requests.

## Example

To analyze "example.com":

**Input:**
```json
{
    "domain": "example.com"
}
```

**Output:**
```json
{
    "domain": "example.com",
    "error": "",
    "domain_authority": 93,
    "page_rank": 8.1,
    "spam_score": 1,
    "link_propensity": 3.2
}
```

## Support

For questions or issues, please contact the actor maintainer or check the Apify documentation.