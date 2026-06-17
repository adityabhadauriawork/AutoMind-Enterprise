import pandas as pd

from agent.analytics_engine import (
    get_top_loss_products
)


def test_top_loss_products():

    data = {
        "Product Name": ["A", "B", "C"],
        "Profit": [-100, -50, 200]
    }

    df = pd.DataFrame(data)

    result = get_top_loss_products(df)

    assert result.index[0] == "A"