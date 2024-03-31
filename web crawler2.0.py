import urllib.request

num = 0
for line in open('name.txt'):
    print(line)
    num = num + 1
    
    try:
        head = { "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}
        request = urllib.request.Request(line, headers=head)
        data = urllib.request.urlopen(request).read().decode()
        print(data)

        file1 = open("网页"+str(num)+".html", 'w', encoding='UTF-8')
        file1.write(data)
    except:
        continue

