'''

Siswa terbaik


Musim penempatan telah dimulai. Ada jumlah N siswa yang berdiri di luar ruang wawancara dalam antrean,
menunggu wawancara mereka. Diketahui bahwa orang yang pertama kali memiliki lebih banyak kesempatan untuk dipilih.

Semua siswa memiliki nilai yang terkait dengan mereka yang dikenal sebagai kemampuan pemecahan-masalah (KPM).
Semakin tinggi kemampuannya, semakin tinggi peluang seleksi. Sekarang, setiap siswa ingin tahu berapa banyak siswa
di depannya yang memiliki kemampuan pemecahan-masalah lebih tinggi daripada dirinya. Tugas Anda adalah
untuk menghasilkan jawaban ini untuk setiap siswa.


Input specification:

input1: Sebuah integer N, yang menunjukkan jumlah siswa yang ada.
input2: Sebuah array A ukuran N, yang menunjukkan kemampuan pemecahan-masalah dari siswa di mana A[i]
menunjukkan KPM milik siswa ke-i dari depan barisan antrian.

Spesifikasi Output:
Array ukuran N yang menunjukkan jawaban untuk setiap siswa.

Contoh:
input1: 6
input2: {4,9,5,3,2,10}

Output: {0,0,1,3,4,0}

Penjelasan:
Siswa pertama tidak memiliki seorang pun di depannya. Jadi, jawabannya adalah 0.
Siswa kedua memiliki KPM lebih besar dari yang pertama. Jadi, jawabannya adalah 0.
Siswa ketiga: 9 lebih besar dari 5. Jadi, jawabannya adalah 1.
Siswa keempat: 9,4 dan 5 lebih besar dari 3. Jadi, jawabannya adalah 3.
Siswa kelima: 3,5,9 dan 4 lebih besar dari 2. Jadi, jawabannya adalah 4.
Siswa keenam: Tidak ada yang di depan yang memiliki KPM lebih besar. Jadi, jawabannya adalah 0.

'''


n = input('jumlah siswa: ')     # if you using python 2, raw_input('jumlah siswa: ')
n = int(n)
kpm_arr = []

for i in range(n):
    kpm = input(f'KPM siswa ke-{i}: ')
    kpm = int(kpm)
    kpm_arr.append(kpm)

output = []
for i, my_kpm in enumerate(kpm_arr):

    if i == 0:
        output.append(0)
        continue

    count = 0
    for j in range(i+1):
        if kpm_arr[j] > my_kpm:
            count += 1
    output.append(count)

print('Output: ' + str(output))
