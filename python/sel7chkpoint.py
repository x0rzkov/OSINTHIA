from selenium import webdriver

op = webdriver.ChromeOptions()
op.add_argument('headless')


dv = '//*[@id="main-content-column"]/div'

sprice = '/div[1]/div[2]/div[3]/span[1]'
dchange = '/div[1]/div[2]/div[3]/span[2]/span[1]'
pchange = '/div[1]/div[2]/div[3]/span[2]/span[2]/span'
ddate = '/div[4]/div/div[1]/strong[1]'
exdate = '/div[3]/div[1]/div/div[2]/select/option[1]'
iv = '/div[4]/div/div[2]/div/strong'


file = 'stocks.txt'
location = './%s' % file
string = open(location, 'r')
stocks = string.read()
string.close()


for i in stocks.split('\n'):
    slist = []
    slist.append(i)
    for s0 in slist:
        driver = webdriver.Chrome(options=op)
        dvxp = driver.find_element_by_xpath

        url = 'https://www.barchart.com/stocks/quotes/%s/options' % s0
        driver.get(url)

        s1 = dvxp(dv + sprice)
        s2 = dvxp(dv + dchange)
        s3 = dvxp(dv + pchange)
        s4 = dvxp(dv + ddate)
        s5 = dvxp(dv + exdate)
        s6 = dvxp(dv + iv)

        print("Stock Name: %s\nPrice: %s\nDollar Change: %s\nPercent Change: %s\nDays to Expiration: %s\nExpiration Date: %s\nImplied Volatility: %s\n" % (s0, s1.text, s2.text, s3.text, s4.text, s5.text, s6.text))


        #dvrelm = driver.find_element_by_xpath('//*[@id="main-content-column"]/div')




# output
#Stock Name: UBER
#Price: 33.62
#Expiration: 2020-05-22 (w)

"""
Stock Name: UBER
Price: 33.62
Dollar Change: +1.15
Percent Change: +3.54%
Days to Expiration: 4 Days
Expiration Date: 2020-05-22 (w)
Implied Volatility: 78.53%

Stock Name: SQ
Price: 76.63
Dollar Change: -3.63
Percent Change: -4.52%
Days to Expiration: 4 Days
Expiration Date: 2020-05-22 (w)
Implied Volatility: 60.02%

Stock Name: MDB
Price: 194.17
Dollar Change: -2.11
Percent Change: -1.07%
Days to Expiration: 4 Days
Expiration Date: 2020-05-22 (w)
Implied Volatility: 69.58%
"""
