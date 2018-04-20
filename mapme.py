"""
INPUT: "!#%&'()*+,-.0123456789:;<=>?
        @ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~"
OUTPUT:
        "[0:[@,`],1:[!,A,a],2:[B,b],3:[#,C,c],4:[D,d],5:[%,E,e],6:[&,F,f],7:[',G,g],8:[(,H,h],9:[),I,i],10:[*,J,j],11:[+,K,k],12:[,,L,l],13:[-,M,m],14:[.,N,n],15:[O,o],16:[0,P,p],17:[1,Q,q],18:[2,R,r],19:[3,S,s],20:[4,T,t],21:[5,U,u],22:[6,V,v],23:[7,W,w],24:[8,X,x],25:[9,Y,y],26:[:,Z,z],27:[;,[,{],28:[<,|],29:[=,],}],30:[>,^,~],31:[?,_]]"
"""


def mapMe(s):
    r = {}
    for x in s:
        i = ord(x) % 32
        r.setdefault(i, [])
        r[i].append(x)
    for k in r:
        print k
    if not r:
        return "[]"
    return '[' + ','.join(['%s:%s' % (k, '[' + ','.join(r[k]) + ']') for k in r]) + ']'


test = "80("
print mapMe(test)
# a = {24:24, 8:8, 16:16}
# print a
# for x in a:
#     print x
{45: {'config_id': 95, 'statement_id': 802, 'journal_id': 7, 'session_id': [261], 'account_id': 12},
 43: {'session_id': []},
 44: {'config_id': 94, 'session_id': []},
 10: {'config_id': 96, 'session_id': []},
 11: {'statement_id': 799, 'journal_id': 7, 'session_id': [260], 'account_id': 12},
 12: {'config_id': 97, 'session_id': []},
 13: {'config_id': 98, 'statement_id': 796, 'journal_id': 7, 'session_id': [259], 'account_id': 12},
 14: {'config_id': 99, 'statement_id': 793, 'journal_id': 7, 'session_id': [258], 'account_id': 12},
 15: {'config_id': 100, 'session_id': []}}
