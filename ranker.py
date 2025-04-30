alpha_set = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9','k':'10','l':'11','m':'12','n':'13','o':'14','p':'15','q':'16','r':'17','s':'18','t':'19','u':'20','v':'21','w':'22','x':'23','y':'24','z':'25'}
word = input("Enter the word: ")
word_list = list(word)
l = []
final = []

for i in range(len(word)):
    r = alpha_set.get(word_list[i])
    l.append(r)


for i in range(len(l)):
    x = max(l)
    final.append(x)
    l.remove(x)

print(final)
print(l)
print(final)

def facto(n):
    a = 1
    for i in range(n):
        a = a*(i+1)
    return a

