
import string

letters = list(string.ascii_letters+'.?!, ')
codes = list('#$%&()*+-/:;<=>@[\]^_`{|}~'+string.ascii_uppercase+'.?!, ')
letters.append('\n')
codes.append('\n')

ltcdict = {}
ctldict = {}

for i in range(len(letters)):
    ltcdict[letters[i]] = codes[i]
    ctldict[codes[i]] = letters[i]




def decode(object):


    rawletter = []
    val = ''
    

    for item in object:
        rawletter.append(item)

    for item in rawletter:
        x = rawletter.index(item)
        rawletter.remove(item)
        rawletter.insert(x, ctldict[item])


    for item in rawletter:
        val = val + str(item)

    return val



def encode(object):

    rawletter = []
    val = ''

    for item in object:
        rawletter.append(item)

    for item in rawletter:
        x = rawletter.index(item)
        rawletter.remove(item)
        rawletter.insert(x, ltcdict[item])

    for item in rawletter:
        val = val + str(item)

    return val


