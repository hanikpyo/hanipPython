html_file = open('index2.html', 'w')
a = ['f','d','s','a']
x = -1
scope = vars()
data = ''
for i in a: #TIP: use a generator
    scope['x']+=1
    data += a[x]
    data += '\n'
html_file.write(data)
html_file.close()