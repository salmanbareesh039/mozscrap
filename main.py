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

        result = {"domains": domain}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(API_URL, json={"domains": [domain]}) as resp:
                    data = await resp.json()

                    if not data or not data[0].get("success"):
                        result["error"] = "No data returned"
                    else:
                        metrics = data[0]["data"][0]["data"]

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

