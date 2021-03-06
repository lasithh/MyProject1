import datetime

from MyInvestementsManager.DividendsManager.devidend_data_processor import getAggrigatedDividendData
from MyInvestementsManager.DividendsManager.dividend_extractor import read_latest_dividends
from MyInvestementsManager.DividendsManager.dividend_store import store_dividends, get_dividends
from MyInvestementsManager.models import ListedCompany, Dividend


def retrieve_store_latest_dividends():
    print("Store Dividends")
    Dividend.objects.all().delete()
    all_companies = ListedCompany.objects.all()
    for company in all_companies:
        symbol = company.symbol
        dividends = read_latest_dividends(symbol)
        store_dividends(dividends)


def retrieve_aggrigated_div_data(dividends):
    print("Retrieve Aggrigated Dividend Data")
    return getAggrigatedDividendData(dividends)


def get_div_data(company):
    return get_dividends(company)


