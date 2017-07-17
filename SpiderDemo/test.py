#coding:utf-8

def read_url_from_file(file_name):
    f = open(file_name,'r')
    length = len(f.readlines())
    f.close()

    f = open(file_name,'r')
    result = list()
    for i in range(int(length/2)):
        name = f.readline()
        link = f.readline()
        name = ''.join(name).strip('\n')
        link = ''.join(link).strip('\n')
        # print(name)
        # print(link)

        result.append({'name':name, 'link':link})
    f.close()
    return result
urls = read_url_from_file('movies3')

print(urls[0]['name'])