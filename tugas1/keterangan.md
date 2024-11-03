1. mengimport modul json .
2. buka file messages.json, parse menggunakan json.load, dan simpan ke variable messages.
3. buka file chats.json, parse menggunakan json.load, dan simpan ke variable chats.
4. buat dictionary untuk menyimpan informasi channel berdasarkan channel_id; dan didalamnya dikasih tanda jika tdk ada title, username.
5. entitynya di sesuaikanid nya.
6. buat list yang digunakan utk menyimpan pesan yg telah diformat
7. baut for loop utk memproses setiap pesan dalam messages.json dan utk mengubah formatnya.
8. buat beberapa variable utk mengetauhi peer_id nya, channel_id,dan utk mencari title dan username dalam channelnya.
9. di dalam for loop buat variable yg bisa memeriksa apakah ada media         
10. dikasih if utk memuat link pesannya dan tanda jika tdk ada username utk channel.
11. buat variable  utk menyusun data dalam format yang diminta, sesuai yang ada di github
12. setelah itu salin hasil yg sdh di format ke sebuah variable.
13. setelah itu bau tempat utk menyimpan hasil akhir ke dalam file final_messages.json.
14. dikasih print bahwa konverensi selesai; ini utk menandakan project berhasil.