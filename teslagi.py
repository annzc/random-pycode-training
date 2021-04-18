echo hello ini adalah tes
for i in $(seq 5); do echo -n "$i "
done
echo tes selasai
echo
echo kesimpulan:
echo -----------
echo walaupun ekstensi file bukan berupa file shell, asalkan kita beri exec* bit pada file tersebut maka baris baris kode shell tetap akan tereksekusi di samping ekstensi file yang dimiliki.
