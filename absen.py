siswa_absen = 0
jumlah_siswa = 30
list_hadir = []

while siswa_absen <= jumlah_siswa:
    siswa = input('absensi nama: ')
    list_hadir.append(siswa)
    siswa_absen += 1

print(list_hadir)
