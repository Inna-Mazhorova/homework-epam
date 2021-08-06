import json
import re
from functools import reduce
from itertools import chain

import pandas as pd
import requests
from bs4 import BeautifulSoup

"""
Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

Текущая стоимость в рублях (конвертацию производить по текущему курсу, взятому с сайта центробанка РФ)
Код компании (справа от названия компании на странице компании)
P/E компании (информация находится справа от графика на странице компании)
Годовой рост/падение компании в процентах (основная таблица)
Высчитать какую прибыль принесли бы акции компании (в процентах), если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High (справа от графика на странице компании)
Сохранить итоговую информацию в 4 JSON файла:

Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
"""


def get_soup_object(url):
    """function that makes a soup object for all the pages in given url"""
    params = {"p": 1}
    pages = 2
    soup_list = []
    while params["p"] <= pages:

        with requests.get(url, params=params) as response:
            # with requests.get(url) as response:
            soup_list.append(BeautifulSoup(response.text, "lxml"))
            params["p"] += 1

    return soup_list


def get_one_page_soup_object(url):
    """function that makes a soup object for 1 page in given url"""
    with requests.get(url) as response:
        soup = BeautifulSoup(response.text, "lxml")

    return soup


def get_link_from_main_table(soup):
    """function that makes a dictionary of companies names and links to their individual urls"""
    # soup = get_soup_object(url)

    paths_to_companies_names = soup.find_all(
        "td", {"class": "table__td table__td--big"}
    )
    companies_dict = {}

    for item in paths_to_companies_names:
        company_name = item.text.strip("\n")
        href_name = "https://markets.businessinsider.com/" + item.find("a").get("href")
        companies_dict[company_name] = href_name

    return companies_dict


def get_data_from_main_table(soup):
    """function that makes a list of year growth(in percents)"""
    # soup = get_soup_object(url)
    paths_to_data = soup.find_all(
        "span", {"class": ["colorGreen", "colorRed", "colorDefault"]}
    )
    year_growth_list = []
    for i in range(len(paths_to_data)):
        if (i + 1) % 8 == 0:
            year_growth_list.append(float(paths_to_data[i].text.strip("%")))
            # year_growth_list + (paths_to_data[i].text.strip("%"))

    return year_growth_list


def get_all_links(url):
    """function that makes a dictionary of companies names and links to their individual urls for all pages"""
    companies_dict_all_pages = {}

    for i in get_soup_object(url):
        companies_dict_all_pages.update(get_link_from_main_table(i))
    # return [v for v in companies_dict_all_pages.values()][0]
    return companies_dict_all_pages


def get_all_data_from_main_table(url):
    """function that makes a list of year growth(in percents) for all pages"""
    year_growth_list_all_pages = []

    for i in get_soup_object(url):
        year_growth_list_all_pages.append(get_data_from_main_table(i))
    return year_growth_list_all_pages


def get_data_from_individual_company_pages(url):
    """function that parses individual company's url and forms a dataframe with company_code, current_price, p/e ratio and potential_profit"""
    individual_company_data = []

    soup = get_one_page_soup_object(url)

    company_code = (
        soup.find("meta", {"name": "description"}).get("content").split(":")[0]
    )
    current_price = float(
        soup.find("span", {"class": "price-section__current-value"}).text.replace(
            ",", ""
        )
    )
    try:
        p_e_ratio = float(
            soup.find(
                "div", {"class": "snapshot__header"}, string="P/E Ratio"
            ).previous_sibling
        )
    except AttributeError:
        p_e_ratio = 0

    try:
        week_52_low = float(
            soup.find("div", {"class": "snapshot__header"}, string="52 Week Low")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        week_52_low = 1

    try:
        week_52_high = float(
            soup.find("div", {"class": "snapshot__header"}, string="52 Week High")
            .previous_sibling.strip()
            .replace(",", "")
        )
    except AttributeError:
        week_52_high = 0

    unreal_profit_per_year_percent = (week_52_high / week_52_low - 1) * 100

    individual_company_data.append(
        [company_code, current_price, p_e_ratio, unreal_profit_per_year_percent]
    )

    company_df = pd.DataFrame(
        columns=["company_code", "current_price", "P_E", "potential_profit_percent"]
    )
    company_df = company_df.append(
        {
            "company_code": company_code,
            "current_price": current_price,
            "P_E": p_e_ratio,
            "potential_profit_percent": unreal_profit_per_year_percent,
        },
        ignore_index=True,
    )

    return company_df


def get_all_data_from_individual_company_pages(url):
    """function that makes a dataframe out of individual_company_pages"""
    url_list = [v for v in get_all_links(url).values()]
    # companies_df = pd.DataFrame(columns=["company_code", "current_price", "P_E", "potential_profit_percent"])
    companies_df = get_data_from_individual_company_pages(url_list[0])

    # for i in range(1, 4):
    for i in range(1, len(url_list)):
        next_company_df = get_data_from_individual_company_pages(url_list[i])
        companies_df = pd.concat([companies_df, next_company_df], ignore_index=True)

    return companies_df


def combine_data_from_individual_and_main(url):
    """function that makes a dataframe out of individual_company_pages and main_page"""
    companies_df = get_all_data_from_individual_company_pages(url)
    year_growth = list(chain.from_iterable(get_all_data_from_main_table(url)))
    companies_df["year_growth"] = pd.Series(year_growth, index=companies_df.index)

    return companies_df


print(
    combine_data_from_individual_and_main(
        "https://markets.businessinsider.com/index/components/s&p_500"
    )
)
