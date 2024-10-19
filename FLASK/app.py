from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_currency_rate(symbol):
    try:
    
        url = f"https://www.google.com/finance/quote/{symbol}"
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

       
        price = soup.find('div', {'class': 'YMlKec fxKbKc'}).text
        
        return price
    except Exception as e:
        return str(e)

@app.route('/')
def index():
   
    usdtry = get_currency_rate('USD-TRY')
    eurtry = get_currency_rate('EUR-TRY')

    return render_template('index.html', usdtry=usdtry, eurtry=eurtry)

if __name__ == '__main__':
    app.run(debug=True)




    

