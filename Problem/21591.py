wc, hc, ws, hs = map(int, input().split())
spareW, spareH = wc-ws, hc-hs

if spareW >=2 and spareH >= 2:
    print(1)
else:
    print(0)
