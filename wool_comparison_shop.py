import requests

from websites import wollplatz

# specifices supported attributes and defines the functions that query them
supported_attributes = {
    'price': 'get_price',
    'delivery_time': 'get_delivery_time',
    'needle_size': 'get_needle_size',
    'materials': 'get_materials',
}
supported_shops = {
    'Wollplatz': wollplatz,
}


def answer_query(brand, product, shopname, attributes):

    session = requests.Session()
    try:
        shop = supported_shops[shopname]
        link_to_product = shop.get_link_to_product(brand, product, session)
    except:
        return [None] * len(attributes)

    # parse page of product
    soup = shop.get_soup(link_to_product, session)

    answers = []
    for attribute in attributes:
        if attribute in supported_attributes and hasattr(shop, supported_attributes[attribute]):
            query_function = getattr(shop, supported_attributes[attribute])
            answer = query_function(soup)
        else:
            answer = None
        answers.append(answer)
    return answers
