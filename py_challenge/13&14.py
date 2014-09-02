__author__ = 'congliu'


# 13
#import xmlrpc.client
#
#url = 'http://www.pythonchallenge.com/pc/phonebook.php'
#server = xmlrpc.client.ServerProxy(url)
#print(server.system.listMethods())
#print(server.system.methodHelp('phone'))
#phone = server.phone('Bert')
#print(phone)


#14
#from PIL import Image
#import urllib.request
#
#url = 'http://www.pythonchallenge.com/pc/return/wire.png'
#f = urllib.request.urlopen(url)
#with open('wire.png','wb') as d_image:
#    d_image.write(f.read())
#
#im = Image.open('wire.png')
#new = Image.new(im.mode,[100,100])
#doubled_steps=200
#directions=[(1,0), (0,1), (-1,0), (0,-1)] # vectors in [x,y] format
#x,y,p=-1,0,0
#while doubled_steps//2 > 0:
#    for v in directions: # we will be taking steps in 4 directions
#        steps=doubled_steps//2
#        for s in range(steps):
#            x,y=x+v[0],y+v[1]
#            new.putpixel((x,y),im.getpixel((p,0)))
#            p+=1
#        doubled_steps-=1
#new.save('14.jpg')


