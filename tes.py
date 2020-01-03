baca= open('coba.txt',encoding='utf-8').readlines()

allisi,alljudul = [],[]
for i in baca:
    try:
        judul,isi = i.strip().split('\t')
    except:
        continue
    judul = str.lower(judul)
    for j in ['iman','shalat','zakat','puasa','haji']:
        if j in judul:
            judul = j
            break
    allisi.append(isi)
    alljudul.append(judul)

for i in ['iman','shalat','zakat','puasa','haji']:
    count = 0
    for x,j in enumerate(alljudul):
        if i == j:
            count += 1
            f = open((i)+str(count)+'.txt','w',encoding='utf-8')
            f.write(allisi[x])
            f.close()
