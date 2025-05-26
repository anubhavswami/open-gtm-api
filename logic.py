def suggest_framework(data):
    if 'enterprise' in data.audience.lower():
        return "Sales-led GTM"
    elif 'community' in data.growth.lower():
        return "Community-led GTM"
    elif 'freemium' in data.pricing.lower():
        return "PLG (Product-led Growth)"
    else:
        return "Hybrid GTM"
