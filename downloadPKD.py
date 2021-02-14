'''downloadPKD.py'''
# Mini wersja: sciaga excela 
# do odpowiedniego folderu przenosi
# Bardziej rozbudowana: w poniedzialek sciaga z soboty, niedzieli i poniedzialku.


from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://www.pse.pl/dane-systemowe/plany-pracy-kse/plan-koordynacyjny-dobowy-pkd/wielkosci-podstawowe')
