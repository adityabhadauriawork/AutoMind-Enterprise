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


def executive_router(df):

    ceo_report = ceo_analysis(df)

    finance_report = finance_analysis(df)

    marketing_report = marketing_analysis(df)

    data_report = data_scientist_analysis(df)

    final_report = f"""

    ### 👔 CEO Strategic Analysis

    {ceo_report}

    ---

    ### 💰 Finance Analysis

        {finance_report}

        ---

    ### 📈 Marketing Analysis

    {marketing_report}

    ---

    ### 📊 Data Science Analysis

    {data_report}

    """

    return final_report