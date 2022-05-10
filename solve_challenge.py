import pandas as pd

from wool_comparison_shop import WoolComparisonShop


def main():
    queries = [
        ['DMC', 'Natura XL', 'Wollplatz'],
        ['Drops', 'Safran', 'Wollplatz'],
        ['Drops', 'Baby Merino Mix', 'Wollplatz'],
        ['Hahn', 'Alpacca Speciale', 'Wollplatz'],
        ['Stylecraft', 'Special double knit', 'Wollplatz'],
    ]
    attributes_of_interest = ['price', 'delivery_time', 'needle_size', 'materials']
    wool_comparison_shop = WoolComparisonShop()

    solution = []
    for query in queries:
        brand, product, shopname = query
        answer = wool_comparison_shop.answer_query(brand, product, shopname, attributes_of_interest)
        solution.append(query + answer)

    dataframe = pd.DataFrame(solution, columns=['brand', 'product', 'shopname'] + attributes_of_interest)
    print(dataframe)
    dataframe.to_csv('solution.csv')


if __name__ == '__main__':
    main()
