def detect_intent(question):

    question = question.lower()

    if any(word in question for word in [
        "state",
        "texas",
        "california",
        "florida",
        "new york"
    ]):
        return "state"

    elif any(word in question for word in [
        "product",
        "products",
        "item",
        "items"
    ]):
        return "product"

    elif any(word in question for word in [
        "category",
        "sub-category",
        "furniture",
        "technology",
        "office supplies"
    ]):
        return "category"

    elif any(word in question for word in [
        "forecast",
        "future",
        "prediction",
        "predict"
    ]):
        return "forecast"

    else:
        return "executive"


def extract_state(question):

    question = question.lower()

    states = [
        "texas",
        "california",
        "florida",
        "new york",
        "washington"
    ]

    for state in states:

        if state in question:

            return state.title()

    return None