class Homework_3():
    def function (angka_1, angka_2, operasi):
        import math
        if operasi == "plus1":
            while angka_1 < angka_2:
                angka_1 += 1
                print(angka_1, end=' ')

        elif operasi == "fibonacci":
            while angka_1 < angka_2:
                angka_1 = angka_1
                angka_2 = angka_2
                angka_3 = ((5 * angka_1 * angka_1) + 4)
                angka_4 = ((5 * angka_1 * angka_1) - 4)
                angka_5 = math.sqrt(angka_3)
                angka_6 = math.sqrt(angka_4)

                if angka_5 % 1 == 0 or angka_6 % 1 == 0:
                    print(str(angka_1), end=' ')
                angka_1 = angka_1 + 1

        elif operasi == "kuadrat":
            n = 0
            while angka_1 < angka_2:
                angka_1 = 2 ** n
                n += 1
                print(angka_1, end=' ')
     
    print(function(2,10,"plus1"))
    print(function(2,120,"fibonacci"))
    print(function(2,10,"kuadrat"))
