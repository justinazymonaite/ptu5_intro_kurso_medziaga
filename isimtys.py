# pirmas budas
# print('dalybos programele')
# sk1 = int(input('iveskite skaiciu: '))
# sk2 = int(input('iveskite skaiciu: '))
# if sk2 == 0:
#     print('dalyba is 0 negalima')
# else:
#     print(sk1/sk2)

# antras budas
print('dalybos programele')
try:
    sk1 = int(input('iveskite skaiciu: '))
    sk2 = int(input('iveskite skaiciu: '))
    atsakymas = sk1/sk2
except ValueError:
    print('ivestas ne skaicius')
except ZeroDivisionError:
    print('dalyba is 0 negalima')
else: # jei ivyko klaida, tai else saka nevykdoma
    print(atsakymas) 
finally: # finally dali programa vykdo ir jei ivyko klaida
    print('programa vis dar veikia iki dabar')

