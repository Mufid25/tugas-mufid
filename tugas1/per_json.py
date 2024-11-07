# 1. Mengimport modul json
import json

# 2. Membuka file chats.json, parse menggunakan json.load, dan simpan ke variable chats
with open('chats.json', 'r', encoding='utf-8') as f:
    chats = json.load(f)

# 3. Membuka file messages.json, parse menggunakan json.load, dan simpan ke variable messages
with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

# 4. Membuat dictionary untuk menyimpan informasi channel berdasarkan channel_id dengan key 'title' dan 'username'
# 5. Menambahkan get() untuk menangani ketiadaan key 'title' dan 'username'
chats_dict = {
    # 6. entitynya di sesuaikan id nya
    chat["entity"]["id"]: {
        "title": chat["entity"].get("title", "Unknown Title"),
        "username": chat["entity"].get("username", None)
    }
    # 7. for loop utk mefilter elemen - elemen dari chats_dict yg memiliki properti entity dgn properti id yg valid utk diperoses.
    for chat in chats
    if "entity" in chat and "id" in chat["entity"]
}

# 8. Membuat list yang digunakan untuk menyimpan pesan yang telah diformat
formatted_messages = []

# 9. foor loop utk memproses setiap pesan dalam messages.json dan mengubah formatnya
for message in messages:
    # 10. disini ada beberapa variabel untuk mengetaui peer_id, channel_id, title, dan username dalam channelnya
    peer_id = message.get("peer_id", {})
    channel_id = peer_id.get("channel_id")
    chat_info = chats_dict.get(channel_id, {"title": "Unknown Channel", "username": None})
    message_id = message.get("id", "Unknown ID")
    
    # 11. variable utk memeriksa apakah ada media dalam pesan
    has_media = message.get("media") is not None

    # 12. if utk membuat link pesan, atau tanda jika tidak ada username untuk channel
    if chat_info["username"]:
        message_link = f"https://t.me/{chat_info['username']}/{message_id}"
    else:
        message_link = "Link not available"

    # 13. variable utk menyusun data dalam format yang diminta
    formatted_message = {
        "page_content": message.get("message", ""),
        "metadata": {
            "channel_id": str(channel_id) if channel_id else "Unknown Channel ID",
            "channel_title": chat_info["title"],
            "has_media": has_media,
            "message_id": message_id,
            "message_link": message_link
        }
    }
    
    # 14. Menambahkan pesan yang diformat ke list formatted_messages
    formatted_messages.append(formatted_message)

# 15. variable utk menyalin hasil yang sudah diformat ke dalam variabel final_messages
final_messages = formatted_messages

# 16. Membuka file final_messages.json untuk menulis hasil akhir dalam format JSON
with open('final_messages.json', 'w', encoding='utf-8') as f:
    json.dump(final_messages, f, ensure_ascii=False, indent=4)

# 17. print utk menampilkan pesan bahwa konversi selesai
print("Proses konversi selesai. Hasilnya disimpan dalam 'final_messages.json'")
