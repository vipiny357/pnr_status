from bs4 import BeautifulSoup
import time
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

timeofday=int(time.strftime('%H''%M'))
if (timeofday>=0 and timeofday<=30) or (timeofday>=2329 and timeofday<=2359):
    print("Availability and prediction may not be available from 11:30 PM to 12:30 AM")
else:


    pre_url_1="https://www.railrestro.com/check-pnr-status?pnr="
    pre_url_2="https://www.railmitra.com/pnr-status?pnr="
    try:
        pnr=str(input())
        if len(pnr)==10:
            url_1=pre_url_1+pnr
            url_2=pre_url_2+pnr
            res=requests.get(url_1,headers=headers)
            res1=requests.get(url_2,headers=headers)
            if res.status_code==200:
                soup = BeautifulSoup(res.text,'lxml')
                aa=soup.find('table',class_='table table-striped table-sm')
                ab=aa.findAll('td')
                ac=ab[2]
                print(ac.text)
            elif  res1.status==200:
                soup = BeautifulSoup(res1.text,'lxml')
                aa=soup.find('table',class_='table table-sm')
                ab=aa.findAll('td')
                ac=ab[1]
                print(ac.text)
            else:
                print("sites not working")
        else:
            print("Pnr Not Correct")
    except:
        print("something unexpected happpened.Please report to the admin")