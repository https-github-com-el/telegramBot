#from time import sleep
#import requests
from bs4 import BeautifulSoup as bs

page = r'c:\Users\ENOON\Desktop\templates\fb.html'  #   target page
#Duration = 10   # length of time difference to write a new image link

#p = requests.get(page)
with open(page,'r') as p:
    soup = bs(p,'html.parser')
    cur = soup.findAll("div")