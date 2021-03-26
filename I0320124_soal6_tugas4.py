#Soal 6


a = 4
b = 11

print('nilai :',a,' , biner :',format(a,'08b'))
print('nilai :',b,' , biner :',format(b,'08b'))

print('==============(|)=====================')
print('nilai :',a,' , biner :',format(a,'08b'))
print('nilai :',b,' , biner :',format(b,'08b'))
print('-------------(4|11)-------------------')
print('nilai :',a|b,' , biner :',format(a|b,'08b'))

print('==============(>>)====================')
print('nilai :',a,' , biner :',format(a,'08b'))
print('nilai :',b,' , biner :',format(b,'08b'))
print('--------------(4>>11)-----------------')
print('nilai : ',a>>b,' , biner :',format(a>>b,'08b'))

print('==============(^)=====================')
print('nilai :',a,' , biner :',format(b,'08b'))
print('nilai :',a,' , biner :',format(b,'08b'))
print('--------------(4^11)------------------')
print('nilai : ',a^b,' , biner :',format(a^b, '08b'))

print('==============(~)=====================')
print('nilai :',a,' , biner :',format(a,'08b'))
print('nilai :',b,' , biner :',format(b,'08b'))
print('--------------(~a)--------------------')
print('nilai : ',~a,', biner :',format(~a,'08b'))

print('==============(&)=====================')
print('nilai :',a,' , biner :',format(a,'08b'))
print('nilai :',b,' , biner :',format(b,'08b'))
print('---------------(b&a)------------------')
print('nilai : ',b&a,' , biner :',format(b&a,'08b'))