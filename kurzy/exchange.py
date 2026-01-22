import httpx

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=3A944C141DC0CF50D37BA4C05DDF5A27')
print(r.text)
print(r.status)
lines = r.text.split('\n')
print(lines[0])
