
#! 17.04.2023


from pytube import YouTube

a = 0

def again():
    while True:
        global a # global değişkeni kullanmak için
        continue_download = input("""
Do you want to do another download ? (Y/N)""")
        if continue_download == "Y" or continue_download == "y":
            a = 0
            break
        elif continue_download =="N" or continue_download == "n":
            a = 1
            print("""
        |---------------------------------------------------------------|    
        |    ღ(¯`◕‿◕´¯) ♫ ♪ ♫ See you later sir ... ♫ ♪ ♫ )¯´◕‿◕`¯(ღ    |
        |---------------------------------------------------------------|   
            """)
            break
        else:
            print("Yes or No ? (Y/N)")
            continue
        
try:
    while a == 0:
        try:
            video_url = input("""
            
    __________________________________________________________________________________________________________
    | __     __         _         _            _____                      _                 _  by Hud4vend1gar|
    | \ \   / /        | |       | |          |  __ \                    | |               | |                |
    |  \ \_/ /__  _   _| |_ _   _| |__   ___  | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __       |
    |   \   / _ \| | | | __| | | | '_ \ / _ \ | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|      |
    |    | | (_) | |_| | |_| |_| | |_) |  __/ | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |         |
    |    |_|\___/ \__,_|\__|\__,_|_.__/ \___| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|         |
    |_________________________________________________________________________________________________________|                                                                                                   
            
--> Enter video url: """)
            if video_url == "quit":
                print("""
            |---------------------------------------------------------------|    
            |    ღ(¯`◕‿◕´¯) ♫ ♪ ♫ See you later sir ... ♫ ♪ ♫ )¯´◕‿◕`¯(ღ    |
            |---------------------------------------------------------------|   
                """)
                break
            video = YouTube(video_url)
        except:
            print("""
            !!! Enter a valid youtube video url !!!""")
            continue
        print(f"Video Title: {video.title}")
        print("""
        1) High Resolution
        2) Low Resolution
        """)

        try:
            resolution_option = int(input("Enter an option (1 or 2): "))
        except:
            print("""
    !!! Just enter 1 or 2. It is not as difficult as you think !!!""")
            continue


        if resolution_option == 1:
            download_video = video.streams.get_highest_resolution()
            print(f"Video downloading ({download_video.filesize_mb}mb) ...")
            download_video.download()
            again()

        elif resolution_option == 2:
            download_video = video.streams.get_lowest_resolution()
            print(f"Video downloading ({download_video.filesize_mb}mb) ...")
            download_video.download()
            again()

        else:
            print("Just enter 1 or 2. It is not as difficult as you think.")
            break
except:
    print("We encountered an error , trying again ...")


