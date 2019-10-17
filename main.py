nama = 'Ulung Markho Mayzebe'
program = 'Usaha'

print(f'Program {program} oleh {nama}')


def hitung_usaha(gaya, jarak):
    usaha = gaya * jarak
    print(f'gaya = {gaya}N pada jarak = {jarak}m')
    print(f'Sehingga usaha = {usaha} joule')
    return usaha


usaha = hitung_usaha(100, 5)
usaha = hitung_usaha(300, 70)





nama = 'Ulung Markho Mayzebe'
program = 'massa jenis'

print(f'Program {program} oleh {nama}')


def hitung_massa_jenis(massa, volume):
    massa_jenis = massa / volume
    print(f'massa = {massa}kg dengan volume = {volume}m^3')
    print(f'Sehingga massa jenis = {massa_jenis} kg/m^3')
    return massa_jenis


massa_jenis = hitung_massa_jenis(2, 150)
massa_jenis = hitung_massa_jenis(10, 200)





nama = 'Ulung Markho Mayzebe'
program = 'Hambatan Listrik'

print(f'Program {program} oleh {nama}')


def hitung_hambatan(tegangan, arus):
    hambatan = tegangan / arus
    print(f'tegangan = {tegangan}v dan arus = {arus}A')
    print(f'Sehingga hambatan  = {hambatan}Ohm')
    return hitung_hambatan


hambatan = hitung_hambatan(220, 2)
hambatan = hitung_hambatan(220, 5)