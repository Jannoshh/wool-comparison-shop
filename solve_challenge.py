import pandas as pd

import wool_comparison_shop


# challenge queries
def main():
    queries = [
        ['DMC', 'Natura XL', 'Wollplatz'],
        ['Drops', 'Safran', 'Wollplatz'],
        ['Drops', 'Baby Merino Mix', 'Wollplatz'],
        ['Hahn', 'Alpacca Speciale', 'Wollplatz'],
        ['Stylecraft', 'Special double knit', 'Wollplatz'],
    ]
    attributes_of_interest = ['price', 'delivery_time', 'needle_size', 'materials']

    data = []
    for query in queries:
        brand, product, shopname = query
        answer = wool_comparison_shop.answer_query(brand, product, shopname, attributes_of_interest)
        data.append(query + answer)

    dataframe = pd.DataFrame(data, columns=['brand', 'product', 'shopname'] + attributes_of_interest)
    print(dataframe)
    dataframe.to_csv('solution.csv')


if __name__ == '__main__':
    main()
