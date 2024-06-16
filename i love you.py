import time
import sys


def slow_print(text, delay= 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#สี้ตัวหนั้งสือ
def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


class LoveLetter:
    def __init__(self, recipient, sender):
        self.recipient = recipient
        self.sender = sender
    
    #ใส่ข้อความหรือเพลงที่ต้องการ
    def generate_message(self):
        message = (
            f"ถึง {self.recipient},\n\n"
            "นี้ๆ ถ้าตัวเล็กอ่านอยู่ เค้าอยากจะบอกว่า\n\n"

            "เค้ารักเธอมากที่สุด\n\n"

            "ถึงเค้าจะชอบมึนใส่ ตอบไม่ตรงคำถาม ไม่กล้ายอมรับความจริง\n\n"

            "แต่เธอก็ยังให้โอกาสเค้าเสอม\n\n"

            "เธอจะปากร้าย ดุ นอย งอน งอม น้อยใจ\n\n"

            "เค้าก็จะบอกตรงนี้ ว่า\n\n"


            "ไม่เคยคิดว่าจะเปิดใจ\n\n"
            "ที่จะรักใครได้อีกแล้ว\n\n"
            "กลัวต้องเสียใจ กลัวต้องร้องไห้\n\n"
            "ถ้าเทความรู้สึกให้ใคร\n\n"

            "แต่โลกพัดเธอผ่านมา\n\n"
            "เหมือนได้พบคนที่ตามหา\n\n"
            "ฉันช่างโชคดี ที่ได้เจอเธอ\n\n"
            "อยากให้เธอได้รู้ว่าฉัน…\n\n"

            "จะตั้งใจรักเธอให้ดี\n\n"
            "จะมีแค่เธอเรื่อยไป\n\n"
            "รักที่เธอให้มา ฉันขอสัญญา\n\n"
            "ว่าจะรักษามันเอาไว้\n\n"
            f"{self.sender}"
        )
        return message
    
    def print_message(self):
        message = self.generate_message()
        colored_message = colored_text(message, 35)
        
        heart_art = colored_text(
            "  ***     ***  \n"
            "******* *******\n"
            " ************* \n"
            "   *********   \n"
            "     *****     \n"
            "      ***      \n"
            "       *       \n", 31)
        slow_print(heart_art, 0.05)
        time.sleep(1)
        slow_print(colored_message, 0.1)

#ชื่อผู้รับ
recipient_name = "แฟน"
#จะใส่ cr.เพลงก็ได้ ใส่ชื่อตัวเองก็ได้
sender_name = "ตั้งใจรัก (happy accident)"


love_letter = LoveLetter(recipient_name, sender_name)


love_letter.print_message()
