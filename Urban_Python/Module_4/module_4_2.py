def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")


    inner_function()    # доступ к функции inner_function() имеется

test_function()
# к функции inner_function() нет доступа вне функции test_function()