
from wool_comparison_shop import WoolComparisonShop


def test_invalid_queries():
    queries = [
        ['Nonsense', 'Natura XL', 'Wollplatz'],
        ['DMC', 'Nonsense', 'Wollplatz'],
        ['DMC', 'Natura XL', 'Nonsense'],
    ]
    attributes_of_interest = ['price', 'delivery_time', 'needle_size', 'materials']
    wool_comparison_shop = WoolComparisonShop()
    
    for query in queries:
        brand, product, shopname = query
        answer = wool_comparison_shop.answer_query(brand, product, shopname, attributes_of_interest)
        assert answer == [None] * len(attributes_of_interest)


def test_valid_queries():
    brand, product, shopname = ['DMC', 'Natura XL', 'Wollplatz']
    attributes_of_interest = ['price', 'delivery_time', 'needle_size', 'materials']
    wool_comparison_shop = WoolComparisonShop()

    answer = wool_comparison_shop.answer_query(brand, product, shopname, attributes_of_interest)
    assert len(answer) == len(attributes_of_interest) and (None not in answer)

    answer = wool_comparison_shop.answer_query(brand, product, shopname, [])
    assert answer == []
