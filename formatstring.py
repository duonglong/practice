import re
format = '{FOO:3}aaaa{BAR:}werwer{BAZ}'
arr = re.findall("\{.*?\}", format)
