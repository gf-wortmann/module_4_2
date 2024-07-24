# Домашняя работа по уроку "Пространство имен."

def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function() # этот вызов работает
inner_function() # этот вызов не работает - функция вне области видимости
