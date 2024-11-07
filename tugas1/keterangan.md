1. mengimport modul json .
2. buka file chats.json, parse menggunakan json.load, dan simpan ke variable chats.
3. buka file messages.json, parse menggunakan json.load, dan simpan ke variable messages.
4. buat dictionary untuk menyimpan informasi channel berdasarkan channel_id; disini ambilah key title, sama username.
5. dan jika tidak dapat menemukan key title dan username, maka kita tambahkan get (membantu menangani ketiadaan key)
6. entitynya di sesuaikan id nya.
7. buat for loop utk mefilter elemen - elemen dari chats_dict yg memiliki properti entity dgn properti id yg valid utk diperoses.
8. buat list yang digunakan utk menyimpan pesan yg telah diformat
9. buat for loop utk memproses setiap pesan dalam messages.json dan utk mengubah formatnya.
10. di dalamnya buat beberapa variable utk mengetauhi peer_id nya, channel_id,dan utk mencari title dan username dalam channelnya; utk mempermudah tambahkan get (membantu menangani ketiadaan key).
11. di dalam for loop buat juga variable yg bisa memeriksa apakah ada media         
12. didalam nya juga dikasih if utk memuat link pesannya dan tanda jika tdk ada username utk channel.
13. setelah itu buat variable  utk menyusun data dalam format yang diminta, sesuai yang ada di github
14. didalam dikasih formatted_messages.append(formatted_message) utk memastikan bahwa setiap pesan yang diformat akan dikumpulkan dalam list formatted_messages.
15. setelah itu salin hasil yg sdh di format ke sebuah variable.
16. buka file final_messages.json menggunakan kode "w" yg artinya write / menulis, dan simpan data final_messages ke dalam file tersebut dalam format JSON menggunakan json.dump.
17. terakhir dikasih print bahwa konverensi selesai; ini utk menandakan project berhasil.