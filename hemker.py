import tele
filters = ['facebook', 'gmail', 'instagram', 'fb', 'ig', 'email', 'ff', 'akun', 'whatsapp']
msg = input('kirim pesan: ')
for f in filters:
    message = f'maaf, tidak ada hack² {f} disini. Diam ya'
    if tele.messages(msg) == 'hack '+f:
        tele.messages(reply, message)
