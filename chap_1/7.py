def sentence(x,y,z):
    s = '{0}時の{1}は{2}'.format(x,y,z)
    return s

x = 12
y = '気温'
z = 22.4
a = sentence(x,y,z)
print(a)
