# utk mengimport json
import json

# digunakan utk membuka dan membaca dari file chats.json dan messages.json
with open('chats.json', 'r', encoding='utf-8') as f:
    chats_data = json.load(f)

with open('messages.json', 'r', encoding='utf-8') as f:
    messages_data = json.load(f)

# utk membuat dictionary yg digunakan agar dapat mengaakses dengan cepat ke informasi channel berdasarkan channel_id
chats_dict = {
    chat["entity"]["id"]: {
        "title": chat["entity"].get("title", "Unknown Title"),
        "username": chat["entity"].get("username", None)
    }
    for chat in chats_data
    if "entity" in chat and "id" in chat["entity"]
}

# utk membuat list yg digunakan utk menyimpan pesan yang telah diformat sesuai kebutuhan
formatted_messages = []

# utk memproses setiap pesan dalam messages.json dan utk mengubah formatnya
for message in messages_data:
    peer_id = message.get("peer_id", {})
    channel_id = peer_id.get("channel_id")
    chat_info = chats_dict.get(channel_id, {"title": "Unknown Channel", "username": None})
    message_id = message.get("id", "Unknown ID")
    
    # memeriksa apakah ada media
    has_media = message.get("media") is not None

    # utk memuat link pesan
    if chat_info["username"]:
        message_link = f"https://t.me/{chat_info['username']}/{message_id}"
    else:
        message_link = "Link not available"  # berfungsi utk menandai jika tidak ada username untuk channel

    # utk meyusun data dalam format yang diminta
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
    formatted_messages.append(formatted_message)

#utk  mensalin hasil yang sudah diformat ke final_messages
final_messages = formatted_messages

# tempat utk menyimpan hasil akhir ke dalam file final_messages.json
with open('final_messages.json', 'w', encoding='utf-8') as f:
    json.dump(final_messages, f, ensure_ascii=False, indent=4)

print("Proses konversi selesai. Hasilnya disimpan dalam 'final_messages.json'")
