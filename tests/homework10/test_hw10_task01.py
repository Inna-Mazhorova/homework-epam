import requests
import requests_mock
from bs4 import BeautifulSoup

from homework10.hw10_task01 import (
    get_data_from_individual_company_pages,
    get_data_from_main_table,
    get_link_from_main_table,
    get_usd_roe,
)


def test_dollar_roe(requests_mock):
    text_dollar_site = '<Valute ID="R01235"><NumCode>840</NumCode><CharCode>USD</CharCode><Nominal>1</Nominal><Name>Доллар США</Name><Value>73</Value>'
    requests_mock.get("http://www.cbr.ru/scripts/XML_daily.asp", text=text_dollar_site)
    assert get_usd_roe() == 73


awaited_company_list = {
    "3M": "https://markets.businessinsider.com//stocks/mmm-stock",
    "A.O. Smith": "https://markets.businessinsider.com//stocks/aos-stock",
    "Abbott Laboratories": "https://markets.businessinsider.com//stocks/abt-stock",
    "AbbVie": "https://markets.businessinsider.com//stocks/abbv-stock",
    "ABIOMED": "https://markets.businessinsider.com//stocks/abmd-stock",
    "Accenture": "https://markets.businessinsider.com//stocks/acn-stock",
    "Activision Blizzard": "https://markets.businessinsider.com//stocks/atvi-stock",
    "Adobe": "https://markets.businessinsider.com//stocks/adbe-stock",
    "Advance Auto Parts": "https://markets.businessinsider.com//stocks/aap-stock",
    "AES": "https://markets.businessinsider.com//stocks/aes-stock",
    "Aflac": "https://markets.businessinsider.com//stocks/afl-stock",
    "Agilent Technologies": "https://markets.businessinsider.com//stocks/a-stock",
    "Air Products and Chemicals": "https://markets.businessinsider.com//stocks/apd-stock",
    "Akamai": "https://markets.businessinsider.com//stocks/akam-stock",
    "Alaska Air Group": "https://markets.businessinsider.com//stocks/alk-stock",
    "Albemarle": "https://markets.businessinsider.com//stocks/alb-stock",
    "Alexandria Real Estate Equities": "https://markets.businessinsider.com//stocks/are-stock",
    "Align Technology": "https://markets.businessinsider.com//stocks/algn-stock",
    "Allegion": "https://markets.businessinsider.com//stocks/alle-stock",
    "Alliant Energy": "https://markets.businessinsider.com//stocks/lnt-stock",
    "Allstate": "https://markets.businessinsider.com//stocks/all-stock",
    "Alphabet A": "https://markets.businessinsider.com//stocks/googl-stock",
    "Alphabet C": "https://markets.businessinsider.com//stocks/goog-stock",
    "Altria": "https://markets.businessinsider.com//stocks/mo-stock",
    "Amazon": "https://markets.businessinsider.com//stocks/amzn-stock",
    "AMD": "https://markets.businessinsider.com//stocks/amd-stock",
    "Ameren": "https://markets.businessinsider.com//stocks/aee-stock",
    "American Airlines": "https://markets.businessinsider.com//stocks/aal-stock",
    "American Electric Power": "https://markets.businessinsider.com//stocks/aep-stock",
    "American Express": "https://markets.businessinsider.com//stocks/axp-stock",
    "American International Group": "https://markets.businessinsider.com//stocks/aig-stock",
    "American Tower": "https://markets.businessinsider.com//stocks/amt-stock",
    "American Water Works": "https://markets.businessinsider.com//stocks/awk-stock",
    "Ameriprise Financial": "https://markets.businessinsider.com//stocks/amp-stock",
    "AmerisourceBergen": "https://markets.businessinsider.com//stocks/abc-stock",
    "Ametek": "https://markets.businessinsider.com//stocks/ame-stock",
    "Amgen": "https://markets.businessinsider.com//stocks/amgn-stock",
    "Amphenol": "https://markets.businessinsider.com//stocks/aph-stock",
    "Analog Devices": "https://markets.businessinsider.com//stocks/adi-stock",
    "ANSYS": "https://markets.businessinsider.com//stocks/anss-stock",
    "Anthem": "https://markets.businessinsider.com//stocks/antm-stock",
    "Aon": "https://markets.businessinsider.com//stocks/aon-stock",
    "APA Corporation Registered Shs": "https://markets.businessinsider.com//stocks/apa-stock",
    "Apple": "https://markets.businessinsider.com//stocks/aapl-stock",
    "Applied Materials": "https://markets.businessinsider.com//stocks/amat-stock",
    "Aptiv": "https://markets.businessinsider.com//stocks/aptv-stock",
    "Archer Daniels Midland": "https://markets.businessinsider.com//stocks/adm-stock",
    "Arista Networks": "https://markets.businessinsider.com//stocks/anet-stock",
    "Arthur J. Gallagher": "https://markets.businessinsider.com//stocks/ajg-stock",
}


def test_getting_links():
    with open("tests/homework10/snp_main_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "lxml")
    assert get_link_from_main_table(soup) == awaited_company_list


awaited_year_growth = [
    22.8,
    45.99,
    23.9,
    22.96,
    4.65,
    41.12,
    2.27,
    41.05,
    31.85,
    37.82,
    53.52,
    66.47,
    -2.68,
    6.85,
    58.46,
    146.03,
    18.63,
    123.17,
    36.78,
    14.36,
    43.52,
    82.44,
    83.03,
    12.53,
    3.66,
    30.41,
    9.97,
    56.58,
    -3.57,
    69.88,
    82.47,
    12.89,
    23.91,
    71.89,
    15.99,
    35.85,
    -4.91,
    35.52,
    45.67,
    14.44,
    32.96,
    42.12,
    11.71,
    31.86,
    96.73,
    86.95,
    41.08,
    70.33,
    34.12,
]


def test_getting_year_growth():
    with open("tests/homework10/snp_main_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "lxml")
    assert get_data_from_main_table(soup) == awaited_year_growth


awaited_data_frame = []


def test_getting_data_from_individual_company_page():
    with open("tests/homework10/snp_individual_page.txt", "r") as file:
        text = file.read()
    soup = BeautifulSoup(text, "lxml")
    company_df = get_data_from_individual_company_pages(soup)
    assert company_df["company_code"][0] == "ADBE"
    assert company_df["current_price"][0] == 47419
    assert company_df["P_E"][0] == 47.1
    assert company_df["potential_profit_percent"][0] == 52.7
