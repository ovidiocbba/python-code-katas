# https://www.codewars.com/kata/5977618080ef220766000022/train/python
def usdcny(usd):
    cny = usd * 6.75
    return f'{cny:.2f} Chinese Yuan'

print(usdcny(465))