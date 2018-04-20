def onlySurviver(p):
   r = p-2**(p.bit_length() - 1)
   return 2*r + 1

for i in range(4, 20):
   print "%s: %s " % (i, onlySurviver(i))
