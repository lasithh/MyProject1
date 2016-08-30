from MyInvestementsManager.models import ListedCompany,\
    CompanyIssuedQuantitiesHistory, DailyTradeSummary, DetailedTrade
from pymongo.database import Database
import datetime

def persistCompaniesList(symbolsToUpdate) :
    """
    This method retrieves a list of symbols in the CSV format and create the models for each of them.
    If the symbol already exists following steps are taken.
    If the quantities of the symbol has been updated, update it on the database. And store the current status on the history table
    """
     #Ignore the first line
    next(symbolsToUpdate, None)

    for item in symbolsToUpdate:
        company = item.decode('utf-8').split(',')        
        
        companyToSave, created = ListedCompany.objects.get_or_create(symbol = company[1], 
                                                                        defaults = {'companyName' : company[0], 
                                                                                    'price' : float(company[2] or 0), 
                                                                                    'issuedQuentity' : int(company[3] or 0), 
                                                                                    'marketCapitalisation' : float(company[4] or 0), 
                                                                                    'marketCapitalisationPercentage' : float(company[5] or 0)},
                                                                        )
        if not created :
            if company[3]  and companyToSave.issuedQuentity != int(company[3]) :
                quantityHistory = CompanyIssuedQuantitiesHistory()
                quantityHistory.issuedQuentity = companyToSave.issuedQuentity
                quantityHistory.marketCapitalisation = companyToSave.marketCapitalisation                
                quantityHistory.marketCapitalisationPercentage = companyToSave.marketCapitalisationPercentage
                quantityHistory.company = companyToSave
                quantityHistory.save()
                
                
                companyToSave.issuedQuentity = int(company[3] or 0)
                companyToSave.marketCapitalisation = float(company[4] or 0)
                companyToSave.marketCapitalisationPercentage = float(company[5] or 0)
                ListedCompany.objects.update(companyToSave)
                

def persistDailyTradingSummary(tradingSummaryInformation):
    """
    Stores the daily trading summary information in the Database. if the data already exists for today, data is updated
    """
    #Skip the line with headers
    next(tradingSummaryInformation, None)
    
    for item in tradingSummaryInformation:
        summary = item.decode('utf-8').split(',')
        

        referencedCompany, created = ListedCompany.objects.get_or_create(symbol = summary[1],
                                                                    defaults = {'companyName' : summary[2], 
                                                                                    'price' : float(summary[14] or 0),
                                                                                    'issuedQuentity' : 0,
                                                                                    'marketCapitalisation' : 0,
                                                                                    'marketCapitalisationPercentage' : 0})
        
        if referencedCompany :
            summarySaved, created = DailyTradeSummary.objects.update_or_create(company = referencedCompany, 
                                                                               date = datetime.date.today(),
                                                                               defaults = {'date' : datetime.datetime.strptime(summary[4], "%Y-%m-%d").date(),
                                                                                           'shareVolume' : int(summary[6] or 0),
                                                                                           'tradeVolume' : int(summary[7] or 0),
                                                                                           'turnover' : float(summary[8] or 0),
                                                                                           'high' : float(summary[9] or 0),
                                                                                           'low' : float(summary[10] or 0),
                                                                                           'priceChange' : float(summary[11] or 0),
                                                                                           'priceChangePercentage' : float(summary[12] or 0),
                                                                                           'lastTradedPrice' : float(summary[14] or 0),
                                                                                           'previouseClose' : float(summary[15] or 0),     
                                                                                           'open' : float(summary[17] or 0),                                                                                      
                                                                                           },
                                                                               )
        
                                                                           
def persistDetailedTrades(detailedTrades):
    """
    Stores the detailed trades information in the Database. if the data already exists for today, data is updated
    """
    #Skip the line with headers
    next(detailedTrades, None)
    next(detailedTrades, None)
    
    for item in detailedTrades:
        trade_part1 = item.decode('utf-8').split(',')
        trade_part2 = next(detailedTrades).decode('utf-8').split(',')

        referencedCompany, created = ListedCompany.objects.get_or_create(symbol = trade_part2[3],
                                                                    defaults = {'companyName' : trade_part2[1], 
                                                                                    'price' : float(trade_part2[5] or 0),
                                                                                    'issuedQuentity' : 0,
                                                                                    'marketCapitalisation' : 0,
                                                                                    'marketCapitalisationPercentage' : 0})
        
        if referencedCompany :
            summarySaved, created = DetailedTrade.objects.update_or_create(company = referencedCompany, 
                                                                               date = datetime.date.today(),
                                                                               defaults = {'date' : datetime.datetime.strptime('2016-08-26', "%Y-%m-%d").date(),                                                                                           
                                                                                           'tradeVolume' : int(trade_part2[7] or 0),
                                                                                           'shareVolume' : int(trade_part2[9] or 0),
                                                                                           'priceChange' : float(trade_part1[13] or 0),
                                                                                           'priceChangePercentage' : float(trade_part2[11] or 0),
                                                                                          
                                                                                           },
                                                                               )
        
        
        
        
        
        