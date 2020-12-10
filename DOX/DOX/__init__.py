import webbrowser
import time
print("|---------------------------------------------------------------- |")
time.sleep(0.2)
print("|DDDDDDDDDDD     |      OOOOOO      |   XXXX             XXXX     |")
time.sleep(0.2)
print("|DD    DDDDDDD   |    OO0    O00    |    XXXX          XXXX       |")
time.sleep(0.2)
print("|DD         DDD  |   000       000  |       XXXX       XXXX       |")
time.sleep(0.2)
print("|DD         DDD  |   000       000  |         XXXX    XXXX        |")
time.sleep(0.2)
print("|DD         DDD  |   000       000  |              XXXX           |")
time.sleep(0.2)
print("|DD         DDD  |    000       000 |          XXXX     XXXX      |")
time.sleep(0.4)
print("|DD         DDD  |    000       000 |       XXXX         XXXX     |")
time.sleep(0.4)
print("|DD      DDDDDD  |     0000   0000  |    XXXX             XXXX    |")
time.sleep(0.4)
print("|DDDDDDDDDDDD    |       0000000    | XXXX                 XXXX   |")
time.sleep(0.4)
print("|-----------------------------------------------------------------|")
time.sleep(0.4)
print("|DOXING TOOL BY HAMZ|---------------------------------------------|")
time.sleep(0.4)
print("|-----------------------------------------------------------------|")
time.sleep(1)
def main():

    Num = input("|    Press 1 for name    |    Press 2 for Number    |    3 for ip tracer   |    Press 4 for discord link    |    5 Settings    |    6 exit    |\n")

    if Num == "1":
        Name = input("Enter name\n")
        Surname = input("Enter surname\n")
        Age = input("Enter age\n")
        print("Hello " + Name + Surname + ", you are " + Age + ".")
        url1 = 'facebook.com/' + Name + Surname
        url2 = 'instagram.com/' + Name + Surname
        url3 = 'Twitter.com/' + Name + Surname
        url4 = 'Twitch.com/' + Name + Surname
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url1)
        webbrowser.get('chrome').open_new_tab(url2)
        webbrowser.get('chrome').open_new_tab(url3)
        webbrowser.get('chrome').open_new_tab(url4)
        log = input("Do you want to save logs?\n")
        if log == "y":
            log = open('Log.txt', 'w')
            log.write('\nUser Name = ' + Name)
            log.write('\nUser Surname = ' + Surname)
            log.write('\nUser Age = ' + Age)
            log.write('\nfacebook.com/' + Name + Surname + Age)
            log.write('\ninstagram.com/' + Name + Surname + Age)
            log.write('\nTwitter.com/' + Name + Surname + Age)
            log.write('\nTwitch.com/' + Name + Surname + Age)

            restart = input("Press y to restart\n").lower()
            if restart == "y".lower():
                main()

        if log == "n":
            restart = input("Press y to restart\n").lower()
            if restart == "y".lower():
                main()


    if Num == "2":
        phone = input("Enter number?\n")
        print('Hi, %s.' % phone)
        url1 = 'WhitePages.com/Phone/' + phone
        url2 = 'who-called.co.uk/Number/' + phone
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url1)
        webbrowser.get('chrome').open_new_tab(url2)
        log = input("Do you want to save logs?\n").lower()
        if log == "y".lower():
            log = open('Log.txt', 'w')
            log.write('User info  = ' + phone)
            log.write('\nWEBSITE = who-called.co.uk/Number/' + phone)
            restart = input("Press y to restart\n").lower()
            if restart == "y".lower():
                main()

        if log == "n":
            restart = input("Press y to restart\n").lower()
            if restart == "y".lower():
                main()


    if Num == "3":
        ip = input("Enter ip")
        url1 = 'ip-tracker.org/locator/ip-lookup.php?ip=' + ip
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url1)
        log = input("Do you want to save logs?\n")
        if log == "y":
            log = open('Log.txt', 'w')
            log.write('User info = ' + ip)
            restart = input("Press y to restart\n")
            if restart == "y":
                main()

        if log == "n":
            restart = input("Press y to restart\n")
            if restart == "y":
                main()

    if Num == "4":
        Disord = input("https://discord.gg/RYGxB4dH----PRESS ENTER")
        log = input("Do you want to save logs?\n")
        if log == "y":
            log = open('Log.txt', 'w')
            log.write('User info = ' + Disord)
            restart = input("Press y to restart\n")
            if restart == "y":
                main()

        if log == "n":
            restart = input("Press y to restart\n")
            if restart == "y":
                main()

    if Num == "5":
        settings = input("Type x for all commands").lower()
        if settings == "x":
            print("Y = YES ////  N = NO ////")
            restart = input("Press y to restart\n").lower()
            if restart == "y".lower():
                main()



    if Num == "6":
        quit()
main()