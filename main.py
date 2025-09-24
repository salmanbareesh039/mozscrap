import whois
from apify import Actor

async def main():
    async with Actor:
        # Get input from Apify (expects { "domains": ["example.com", ...] })
        input_data = await Actor.get_input() or {}
        domains = input_data.get('domains', [])
        results = []
        for domain in domains:
            try:
                w = whois.whois(domain)
                result = {'domain': domain, 'error': ''}
                # Add all parsed whois fields as columns
                if isinstance(w, dict):
                    for k, v in w.items():
                        result[k] = v
                else:
                    # Some whois libraries return an object, not a dict
                    for k in dir(w):
                        if not k.startswith('_') and not callable(getattr(w, k)):
                            result[k] = getattr(w, k)
                results.append(result)
            except Exception as e:
                results.append({'domain': domain, 'error': str(e)})
        # Save results to Apify dataset
        await Actor.push_data(results)
        # Optionally print results for debugging (can be removed in production)
        print(results)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
