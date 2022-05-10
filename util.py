import bs4

# parse link
def get_soup(link, session, strainer=None):
    res = session.get(link)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, features='lxml', parse_only=strainer)


def is_abbreviation(abbrev, text):
    abbrev = abbrev.lower()
    text = text.lower()
    words = text.split()
    if not abbrev:
        return True
    if abbrev and not text:
        return False
    if abbrev[0] != text[0]:
        return False
    else:
        return (is_abbreviation(abbrev[1:],' '.join(words[1:])) or
                any(is_abbreviation(abbrev[1:], text[i+1:])
                    for i in range(len(words[0]))))