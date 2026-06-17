from agent.ceo_agent import (
    ceo_analysis
)

from agent.finance_agent import (
    finance_analysis
)

from agent.marketing_agent import (
    marketing_analysis
)

from agent.data_scientist_agent import (
    data_scientist_analysis
)


def route_agent(question, df):

    question = question.lower()

    # ====================
    # CEO AGENT
    # ====================

    if any(
        word in question
        for word in [
            "strategy",
            "risk",
            "focus",
            "growth",
            "business"
        ]
    ):

        return ceo_analysis(df)

    # ====================
    # FINANCE AGENT
    # ====================

    elif any(
        word in question
        for word in [
            "profit",
            "loss",
            "margin",
            "finance",
            "financial"
        ]
    ):

        return finance_analysis(df)

    # ====================
    # MARKETING AGENT
    # ====================

    elif any(
        word in question
        for word in [
            "marketing",
            "promote",
            "campaign",
            "customer",
            "sales"
        ]
    ):

        return marketing_analysis(df)

    # ====================
    # DATA SCIENTIST AGENT
    # ====================

    elif any(
        word in question
        for word in [
            "forecast",
            "prediction",
            "model",
            "future",
            "trend"
        ]
    ):

        return data_scientist_analysis(df)

    # ====================
    # DEFAULT
    # ====================

    return """
    Agent Router:

    Please ask a question related to:

    • Business Strategy
    • Finance
    • Marketing
    • Forecasting
    """