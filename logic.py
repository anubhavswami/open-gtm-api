def suggest_framework(data):
    """
    Map GTM model using scoring rules based on stage, confidence, and blockers.
    For early-stage companies, recommend the Founder-Led Model.
    """
    # Early stage check (pre-product, MVP, pre-revenue)
    early_stages = ["Pre-product", "MVP built, not launched", "Launched but pre-revenue"]

    # Default to Founder-Led Model for early stage companies as per user story
    if data.stage in early_stages:
        model = "Founder-Led Demand Model"
        rationale = "You're still validating your product and market fit. At this stage, founders should lead demand generation through direct engagement."
        cta = "Sign up to get a detailed playbook for implementing the Founder-Led Demand Model at your startup."
    # Low confidence score indicates need for more structured approach
    elif data.confidence <= 5:
        model = "Structured GTM Framework"
        rationale = "Your confidence level suggests you need a more structured approach to GTM. This framework provides clear steps and metrics."
        cta = "Sign up to access our Structured GTM Framework with templates and execution guides."
    # Check for specific blockers
    elif data.blockers and ("Don't know how to find first users" in data.blockers or "Don't know what to say or how to position the product" in data.blockers):
        model = "Customer Development GTM"
        rationale = "Your challenges suggest you need to focus on customer development and positioning before scaling GTM efforts."
        cta = "Sign up to get our Customer Development Playbook with interview templates and positioning frameworks."
    # Enterprise audience typically needs sales-led approach
    elif 'enterprise' in data.audience.lower():
        model = "Sales-led GTM"
        rationale = "With an enterprise audience, a sales-led approach typically yields the best results for complex products."
        cta = "Sign up to access our Enterprise Sales Playbook with outreach templates and negotiation frameworks."
    # Community growth indicates community-led approach
    elif 'community' in data.growth.lower():
        model = "Community-led GTM"
        rationale = "Your focus on community as a growth channel aligns perfectly with a community-led GTM approach."
        cta = "Sign up to get our Community-Led Growth Playbook with engagement strategies and scaling tactics."
    # Freemium pricing suggests product-led growth
    elif 'freemium' in data.pricing.lower():
        model = "PLG (Product-led Growth)"
        rationale = "Your freemium pricing model is well-suited for a product-led growth strategy where the product itself drives acquisition."
        cta = "Sign up to access our PLG Playbook with activation metrics and conversion optimization tactics."
    # Default case
    else:
        model = "Hybrid GTM"
        rationale = "Based on your inputs, a hybrid approach combining multiple GTM strategies would be most effective for your situation."
        cta = "Sign up to get our Hybrid GTM Framework that combines multiple strategies for maximum impact."

    return {
        "model": model,
        "rationale": rationale,
        "cta": cta
    }
