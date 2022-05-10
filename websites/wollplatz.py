import bs4
from util import is_abbreviation, get_soup


def get_link_to_product(brand, product, session):
    base_link = f'https://www.wollplatz.de/wolle/{brand}'
    strainer = bs4.SoupStrainer('div', class_="productlist-mainholder")

    soup = get_soup(base_link, session, strainer)
    fitting_product = search_for_product(soup, brand, product)

    page = 2
    page_count = get_page_count(soup)
    # search other pages for a fitting product
    while fitting_product is None and page <= page_count:
        soup = get_soup(f'{base_link}?page={page}', session, strainer)
        fitting_product = search_for_product(soup, brand, product)
        page += 1
    link_to_product = fitting_product['href']
    return link_to_product


def search_for_product(soup, brand, product):
    productlist = soup.find_all('a', class_='productlist-imgholder')
    product_titles = [p['title'].replace(brand, '').strip() for p in productlist]
    for p in product_titles:
        if is_abbreviation(p, product) or is_abbreviation(product, p):
            fitting_name = p
            return productlist[product_titles.index(fitting_name)]


def get_page_count(soup):
    pagination = soup.find('span', class_='paginavan')
    page_indexes = pagination.select('b')
    if page_indexes:
        page_count = int(page_indexes[1].text)
    else:
        page_count = 1
    return page_count


def get_price(soup):
    price = soup.find_all('span', class_='product-price')[0]['content']  # doesn't include delivery cost
    price += ' Euros'
    return price


def get_delivery_time(soup):
    availability = soup.find(id='ContentPlaceHolder1_upStockInfoDescription').find('span')['class'][0]
    if availability == 'stock-green':
        delivery_time = '2-3 Werktage' # assumes you're from Germany
    else:
        delivery_time = 'Nicht lieferbar'
    return delivery_time


def get_needle_size(soup):
    table_data = soup.select('td')
    table_data = [td.text for td in table_data]
    needle_size = table_data[table_data.index('Nadelstärke') + 1]
    return needle_size


def get_materials(soup):
    table_data = soup.select('td')
    table_data = [td.text for td in table_data]
    materials = table_data[table_data.index('Zusammenstellung') + 1]
    return materials