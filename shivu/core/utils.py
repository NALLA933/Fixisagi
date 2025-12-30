from html import escape

def to_small_caps(text: str) -> str:
    if not text:
        return text

    table = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ" * 2
    )
    return text.translate(table)

def safe(text):
    return escape(str(text))