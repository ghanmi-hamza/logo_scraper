from scraper import Urls
from config import Base_URL

def main():
    i = 1
    cls = Urls()
    cls.get_browser()
    res = cls.get_url_from_page(Base_URL)
    print(res, len(res))

if __name__ == "__main__":
    main()
