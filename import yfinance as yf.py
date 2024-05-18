import yfinance as yf

def fundamental_analysis(ticker):
        #Get stock Data
        stock=yf.Ticker(ticker)
    
        #Get key statistics
        key_stats=stock.info
    
        #Extract relevant fundamental data
        market_cap=key_stats.get('marketCap',None)
        pe_ratio=key_stats.get('forwardPE',None)
        dividend_yield=key_stats.get('dividendYield',None)
        eps=key_stats.get('trailingEps',None)
        roe=key_stats.get('returnOnEquity',None)
    
        #print fundamental data
        print("Market Cap:",market_cap)
        print("P/E Ratio:",pe_ratio)
        print("Dividend Yield:",dividend_yield)
        print("Earning Per Share (EPS):",eps)
        print("Return on Equity (ROE):",roe)