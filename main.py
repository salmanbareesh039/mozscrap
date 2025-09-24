import aiohttp
from apify import Actor

API_URL = "https://embed.seomator.com/api/moz-metrics"

async def main():
    async with Actor:
        # Get input (expects { "domain": "example.com" })
        input_data = await Actor.get_input() or {}
        domain = input_data.get("domain")
        
        if not domain:
            await Actor.push_data({"error": "No domain provided"})
            return
        
        result = {"domain": domain, "error": ""}
        
        try:
            async with aiohttp.ClientSession() as session:
                payload = {"domains": [domain]}
                print(f"Sending payload: {payload}")
                
                async with session.post(API_URL, json=payload) as resp:
                    print(f"Response status: {resp.status}")
                    data = await resp.json()
                    print(f"Response data: {data}")
                    
                    if not data or not data.get("success", False):
                        result["error"] = f"API returned success=False: {data.get('error', 'Unknown error') if data else 'No data returned'}"
                    else:
                        if "data" not in data or len(data["data"]) == 0:
                            result["error"] = "No metrics data found in response"
                        else:
                            # The data structure is: data["data"][0]["data"] contains the metrics
                            metrics = data["data"][0]["data"]
                            result.update({
                                "domain_authority": metrics.get("moz_domain_authority"),
                                "page_rank": metrics.get("page_rank"),
                                "spam_score": metrics.get("moz_spam_score"),
                                "link_propensity": metrics.get("moz_link_propensity"),
                                "total_pages": metrics.get("moz_pages_to_subdomain"),
                                "external_pages": metrics.get("moz_external_pages_to_subdomain"),
                                "root_domains": metrics.get("moz_root_domains_to_subdomain"),
                                "nofollow_pages": metrics.get("moz_nofollow_pages_to_subdomain"),
                                "redirect_pages": metrics.get("moz_redirect_pages_to_subdomain"),
                                "deleted_pages": metrics.get("moz_deleted_pages_to_subdomain"),
                                "external_nofollow_pages": metrics.get("moz_external_nofollow_pages_to_subdomain"),
                                "external_redirect_pages": metrics.get("moz_external_redirect_pages_to_subdomain"),
                                "nofollow_root_domains": metrics.get("moz_nofollow_root_domains_to_subdomain"),
                            })
        except Exception as e:
            result["error"] = str(e)
        
        # Save result to Apify dataset
        await Actor.push_data(result)
        
        # Debug log
        print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
