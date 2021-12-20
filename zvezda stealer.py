from bs4 import BeautifulSoup
import requests

#HOST = 'https://www.ozon.ru/'
URL = 'https://www.ozon.ru/product/videokarta-palit-geforce-rtx-3060-ti-8-gb-ne6306t019p2-190ad-rev-2-0-lhr-231908039/?asb=NPkYJQz25AWTyLRsXRZCsSpWE%252BxtZ9JuX0Ni7N8Y0AI%253D&asb2=g9EeGyI6q_PaBPmkN69rRxFRZWBpaOTYRugVrF8adngpQGct8BA4Z7S1xXSuwG6R&keywords=3060ti&sh=FFaub92R'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

r = requests.get(URL, HEADERS)
HTML_content = BeautifulSoup(r.text,'html.parser')

#поиск в HTML_content процента звёзд
def zvezdi_founder(content):
    
    zvezdi =  str(content.find_all("div", class_="ui-a0c", limit = 1))
    zvezdi_answer = ''
    #вычленение процента из <div class="ui-a0c" style="width:91.91111111111111%;"></div>
    for i in range (len(zvezdi)):
        if zvezdi[i-1] == ':' and zvezdi[i-2] == 'h':
            while zvezdi[i] !=';':
                zvezdi_answer+= zvezdi[i]
                i+=1
            break
        
    print('Процент звёзд от нуля до ста: ' +zvezdi_answer)

#поиск в HTML_content количества отзывов
def kolvo_otzivov_founder(content):

    #вычленение количества отзывов  из <div class="ui-e6">12 отзывов</div>
    kolvo_otzivov = str(content.find_all("div", class_="ui-e6", limit = 1))
    kolvo_otzivov_answer=''
    for i in range (len(kolvo_otzivov)):
        if kolvo_otzivov[i-1] == '>' and kolvo_otzivov[i-2] == '"':
            while kolvo_otzivov[i]!='<':
                kolvo_otzivov_answer+= kolvo_otzivov[i]
                i+=1
            break
    print( 'количество отзывов: ' + kolvo_otzivov_answer)

#main
if  HTML_content.find_all("div", class_="ui-a0c", limit = 1)!= []:
    zvezdi_founder(HTML_content)
    kolvo_otzivov_founder(HTML_content)

else:
        print('Пока прокси не подключены, перезапустите программу')
    
