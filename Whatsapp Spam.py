import pyautogui
import time

# Kullanıcıdan mesajı ve gönderilecek mesaj sayısını al
message = input("Göndermek istediğiniz mesajı yazın: ")
number_of_messages = int(input("Kaç kez göndermek istersiniz? "))

# WhatsApp Web'i açın ve kişiyle olan sohbeti açın
print("Lütfen WhatsApp Web'i açın ve sohbeti seçin.")
time.sleep(3)  # 3 saniye bekleyin, böylece WhatsApp Web'i açabilirsiniz

# Mesaj gönderme işlemi
for i in range(number_of_messages):
    pyautogui.typewrite(message)  # Mesajı yaz
    pyautogui.press('enter')  # Mesajı gönder
    time.sleep(0.1)  # 0.1 saniye bekle

print("Mesajlar gönderildi!")