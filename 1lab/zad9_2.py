"""
Напишите программу, имитирующую работу банкомата. Выберите
структуру данных для хранения купюр разного достоинства в заданном
количестве. При вводе пользователем запрашиваемой суммы денег,
скрипт должен вывести на консоль количество купюр подходящего
достоинства. Если имеющихся денег не хватает, то необходимо
напечатать сообщение «Операция не может быть выполнена!».
Например, при сумме 5370 рублей на консоль должно быть выведено
«5*1000 + 3*100 + 1*50 + 2*10».

"""
money_in = {
    '5000':3,
    '1000':1,
    '500':7,
    '100':2,
    '50':7,
    '10':47
}

def bank(summ):
    balance = money_in['5000']*money_in['1000']*money_in['500']*money_in['100']*money_in['50']*money_in['10']
    if summ > balance :
        print ('В банкомате недостаточно средств. Баланс банкомата = ' + str (balance))
    
    m_5000 = summ//5000
    m_1000 = (summ%5000)//1000
    m_500 = (summ%1000)//500
    m_100 = (summ%500)//100
    m_50 = (summ%100)//50
    m_10 = (summ%50)//10
    m_m10 = summ%10

    if m_5000<=money_in['5000']:
        if m_1000<=money_in['1000']:
            if m_500<=money_in['500']:
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
            else:
                razn_500 = m_500 - money_in['500']
                m_500 = m_500 - razn_500
                m_100 = ((summ%500)+(razn_500*500))//100
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
        else:
            razn_1000 = m_1000 - money_in['1000']
            m_1000 = m_1000 - razn_1000
            m_500 = ((summ%1000)+(razn_1000*1000))//500
            if m_500<=money_in['500']:
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
            else:
                razn_500 = m_500 - money_in['500']
                m_500 = m_500 - razn_500
                m_100 = ((summ%500)+(razn_500*500))//100
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
    else:
        razn_5000 = m_5000 - money_in['5000']
        m_5000 = m_5000 - razn_5000
        m_1000 = ((summ%5000)+(razn_5000*5000))//1000
        if m_1000<=money_in['1000']:
            if m_500<=money_in['500']:
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
            else:
                razn_500 = m_500 - money_in['500']
                m_500 = m_500 - razn_500
                m_100 = ((summ%500)+(razn_500*500))//100
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
        else:
            razn_1000 = m_1000 - money_in['1000']
            m_1000 = m_1000 - razn_1000
            m_500 = ((summ%1000)+(razn_1000*1000))//500
            if m_500<=money_in['500']:
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
            else:
                razn_500 = m_500 - money_in['500']
                m_500 = m_500 - razn_500
                m_100 = ((summ%500)+(razn_500*500))//100
                if m_100<=money_in['100']:
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10
                else:
                    razn_100 = m_100 - money_in['100']
                    m_100 = m_100 - razn_100
                    m_50 = ((summ%100)+(razn_100*100))//50
                    if m_50<=money_in['50']:
                        print()
                    else:
                        razn_50 = m_50 - money_in['50']
                        m_50 = m_50 - razn_50
                        m_10 = ((summ%50)+(razn_50*50))//10                     

    print('Рекомендованые номиналы для обналичивания денежных средств: ' + str(m_5000) + '*' + '5000  '+ str(m_1000) + '*' + 
    '1000  '+ str(m_500) + '*' + '500  '+ str(m_100) + '*' + '100  '+ str(m_50) + '*' + '50  '+ str(m_10) + '*' + '10  ')
    print('Остаток на счету: ' + str(m_m10) + ' руб.')    


enter = int (input('Введите сумму: '))
bank(enter)          



