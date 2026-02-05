import httpx

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"

def gettxt():
    r = httpx.get(url)
    return r.text

def geteur(t):
    l = t.split("\n")
    for x in l:
        p = x.split("|")
        if len(p) == 5 and p[3] == "EUR":
            m = int(p[2])
            k = float(p[4].replace(",", "."))
            return k / m

def ch():
    print("1 EUR -> CZK")
    print("2 CZK -> EUR")
    while True:
        a = input("choose or write quit: ")
        if a == "1" or a == "2" or a == "quit":
            return a
        print("wrong input")

def num(txt):
    while True:
        n = input(txt)
        n = n.replace(",", ".")
        try:
            n = float(n)
            if n > 0:
                return n
        except:
            pass
        print("wrong number")

def main():
    try:
        t = gettxt()
        r = geteur(t)
    except:
        print("error loading data")
        return

    print("1 EUR =", r, "CZK")

    while True:
        c = ch()
        if c == "quit":
            print("bye")
            break

        if c == "1":
            e = num("EUR: ")
            print(e, "EUR =", e * r, "CZK")
        else:
            z = num("CZK: ")
            print(z, "CZK =", z / r, "EUR")

main()