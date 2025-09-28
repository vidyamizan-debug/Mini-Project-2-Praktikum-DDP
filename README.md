# Mini-Project-2-Praktikum-DDP
NAMA : VIDYA KHANSA MIZAN\
NIM : 2509116052, SISTEM INFORMASI B'2025\
MATA KULIAH : PRAKTIKUM DASAR-DASAR PEMROGRAMAN

# SISTEM REMINDER TUGAS (2)
Pada Github yang ini, saya akan melampirkan sebuah Flowchart dan pemrograman Python mengenai Sistem Reminder Tugas yang telah saya perbarui. 
Sistem Reminder Tugas ini untuk apa? sistem ini bertujuan untuk membantu kita agar tidak lupa dengan tugas-tugas yang kita miliki, selain itu sistem ini juga melampirkan deadline atau tenggat dari tugas yang telah di input ke dalam sistem. Pada sistem yang telah saya perbarui ini, saya menambahkan fitur baru yaitu fitur Login. Di fitur Login ini kita bisa memilih mau login sebagai "Mahasiswa" ataupun "Admin", namun fitur yang disediakan untuk kedua role/peran ini tentunya berbeda. Dimana jika kita login sebagai "Mahasiswa", kita hanya bisa mengakses list lengkap tugas yang kita miliki dan logout/exit. Sedangkan jika kita login sebagai "Admin", kita bisa mengakses semua menu sesuai yang kita mau, ada Lihat tugas lengkap, Tambah tugas, Update tugas, Hapus tugas, dan tentunya logout/exit.

# FLOWCHART
<img width="4992" height="2102" alt="MinPro 2 drawio" src="https://github.com/user-attachments/assets/00bdac6d-12ba-41f6-bd29-1cea547d758d" />

Gambar diatas ialah flowchart dari program saya.

# ROLE --> MAHASISWA
- Login 
<img width="343" height="212" alt="Screenshot 2025-09-28 213144" src="https://github.com/user-attachments/assets/b8ecf998-65b5-4ff1-87a5-0b337b2028a7" />

Pertama kita akan diberikan 2 pilihan peran, disini kita akan memasukkan no. 1 (Mahasiswa). 

<img width="911" height="613" alt="Screenshot 2025-09-28 212945" src="https://github.com/user-attachments/assets/187b40a9-7cee-4bf8-88d6-efe07279d88a" />

kita akan diberikan 3 kesempatan untuk melakukan login.

<img width="982" height="457" alt="Screenshot 2025-09-28 184518" src="https://github.com/user-attachments/assets/6242dfe9-9fb3-49c6-9ca9-21f806dac5d0" />

ini adalah tampilan jika kita berhasil login **(passsword : 2509116052)**

- Menu Utama 1 (Lihat List Tugas)
<img width="711" height="582" alt="Screenshot 2025-09-28 212041" src="https://github.com/user-attachments/assets/3d42d34c-d819-431f-bb4f-5ddd319643f5" />

Lalu akan muncul tabel berisikan pilihan menu yang bisa kita pilih, disini kita akan memilih nomor 1 yaitu "Lihat List Tugas". Setelahnya sistem akan menampilkan list-list tugas yang kita miliki.

- Menu Utama 2 (Exit)
<img width="681" height="276" alt="Screenshot 2025-09-28 212419" src="https://github.com/user-attachments/assets/7149f169-4a71-4c7d-97c8-53656ed6b8e8" />

seperti tadi, dia akan menampilkan menu pilihan dan kali ini kita akan memilih nomor 2. Maka, sistem akan memberikan output seperti yang ada pada gambar.

# ROLE --> ADMIN
- Login
<img width="313" height="165" alt="Screenshot 2025-09-28 214127" src="https://github.com/user-attachments/assets/fee36648-4044-43be-92c4-648abbd025ff" />

sama seperti di login role mahasiswa, kita akan diberikan 2 pilihan. Namun kali ini kita akan memilih nomor 2.

<img width="906" height="406" alt="Screenshot 2025-09-28 214311" src="https://github.com/user-attachments/assets/d8090fa7-6df2-4c97-95e9-5eab2d5f7d36" />

disini kita juga akan diberikan 3 kesempatan untuk melakukan login.

<img width="794" height="242" alt="Screenshot 2025-09-28 214452" src="https://github.com/user-attachments/assets/07ee871e-31c4-4500-9388-f15f20d0fe8d" />

gambar di atas merupakan tamppilan yang akan kita dapatkan apabila kita berhasil melakuka login **(password : aamiin)**

- Menu Utama 1 (Lihat List tugas)
<img width="686" height="664" alt="Screenshot 2025-09-28 214701" src="https://github.com/user-attachments/assets/211a6217-e1e4-4de7-8137-3e145e522730" />

sama seperti yang di role mahasiswa, akan muncul tabel berisikan pilihan menu yang bisa kita pilih. Disini kita akan memilih nomor 1 yaitu "Lihat List Tugas". Setelahnya sistem akan menampilkan list-list tugas yang kita miliki.

- Menu Utama 2 (Tambah Tugas)
<img width="508" height="450" alt="Screenshot 2025-09-28 215026" src="https://github.com/user-attachments/assets/d75c639c-19cd-4ef2-a9b2-5722c4160e5f" />

pada menu 2 kita bisa menambahkan tugas, dengan cara memasukkan nama tugas yang akan kita tambahkan ke list beserta deadlinenya. Maka sistem akan menyimpan tugas baru itu di dalam list.

<img width="705" height="688" alt="Screenshot 2025-09-28 215310" src="https://github.com/user-attachments/assets/b5d8fb4b-bf66-430e-bacf-723d943b5e1f" />

untuk bisa melihat apakah sudah masuk ke list tugas atau belum, kita bisa cek kembali di menu 1.

- Menu Utama 3 (Update Tugas)
<img width="1050" height="516" alt="Screenshot 2025-09-28 215739" src="https://github.com/user-attachments/assets/2e887a44-800b-45b0-a5dd-2d23a76a215a" />

pada menu ini kita bisa mengubah nama ataupun deadline tugas yang kita miliki di dalam list. Dengan cara memasukkan nama tugas yang ingin kita ubah, lalu mengisi kembali nama tugass dan deadline baru dari tugas yang ingin kita ubah.

<img width="698" height="677" alt="Screenshot 2025-09-28 215901" src="https://github.com/user-attachments/assets/eb9bc39c-96ca-441e-8a41-0ec130b66986" />

sama seperti tadi, kita bisa melihat tabel list dengan mengecek di menu 1.

- Menu 4 (Hapus Tugas)
<img width="826" height="405" alt="Screenshot 2025-09-28 220109" src="https://github.com/user-attachments/assets/dbfc306c-62ea-4c14-949b-9a020ec4004b" />

kita bisa menghapus tugas yang kita miliki di menu ini. Dengan cara memasukkan nama tugas yang ingin kita hapus, lalu sistem akan menghapusnya.

<img width="691" height="668" alt="Screenshot 2025-09-28 220212" src="https://github.com/user-attachments/assets/9c439b6e-abd4-46cb-8180-53ca28ce2896" />

kita bisa mnegecek kembali apakah tugasnya sudah terhapus atau belum di menu 1.

- Menu 5 (Exit)
<img width="673" height="356" alt="Screenshot 2025-09-28 220300" src="https://github.com/user-attachments/assets/5b6fab13-ae0d-4109-9c90-3d5634365fd8" />

di menu ini kita bisa melakukan logout atau keluar, hanya dengan mengetik nomor 5.

- Jika kita memasukkan angka selain 1 atau 2 di laman LOGIN
<img width="448" height="230" alt="Screenshot 2025-09-28 220847" src="https://github.com/user-attachments/assets/04ce9ba1-ac10-4d9e-98a9-be8f52b138af" />

sistem akan menampilkan output seperti itu

- Error Handling yang ada di program ini
<img width="488" height="234" alt="Screenshot 2025-09-28 222135" src="https://github.com/user-attachments/assets/5d3c6a43-05ed-4da1-8429-dd118a70c0b8" />

ini adalah contoh error handling "ValueError"


ini adalah contoh error handling "KeyboardInterrupt"


ini adalah contoh error handling "EOFError"
