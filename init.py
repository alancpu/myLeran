
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
init(storage)

print(storage)


me = 'Magnus Lite Hetlang'
storage['first']['Magnus'] = [me]
storage['middle']['Lite'] = [me]
storage['last']['Hetland'] = [me]

def  store(data,full_name):
    names = full_name.split()
    if len(names) == 2 : names.insert(1,'')
    labels = 'first'.'middle'.'last'



def lookup(data,label,name):
    return data[label].get(name)

x = lookup(storage,'middle','Lite')

print(x)