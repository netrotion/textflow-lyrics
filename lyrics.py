#netrotion - hngl2808
#this code only work on windows, if you want to running on another os, you can customize this script :D
from msvcrt import getch #module nhận diện phím (k dùng)
import winsound #module chơi nhạc
import threading
import random
import shutil
import time
import sys 
import os

ASUKA = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠓⠲⣤⠎⠁⠀⠀⠈⠙⠧⢄⣒⡲⠦⠤⠕⠀⠀⠀⠀⠀⠈⠽⠲⠤⢤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢄⣀⢠⡤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣄⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠊⢀⠔⠁⠀⠀⡠⠒⠀⢠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⡠⡰⠋⠀⠀⡠⠊⠀⠀⠀⡎⢀⠀⠀⠀⡀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡄⠈⢦⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⢠⢃⠞⡰⠁⠀⣴⡿⠁⠀⠀⠀⢸⠁⠸⠀⠀⠀⢆⠀⠘⣆⠀⠀⠀⣄⠀⠀⠀⠀⠀⠈⢦⠀⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣧⠋⡰⠁⢀⣾⣷⠃⠀⠀⢠⣶⣿⠀⡆⠀⠀⠀⢸⠀⠀⡜⣧⡀⠀⠈⢣⡀⢂⠀⠀⠀⠀⠀⠀⠙⠲⣖⡊⠉⠀⠀⠠
⠀⠀⠀⠀⠀⠀⢸⡏⢀⠇⠀⣼⣿⡏⠀⠀⢠⣿⡿⢻⠀⣿⡀⠀⠀⢸⡆⠀⢳⡈⢿⠀⠀⠀⠱⡄⠑⣄⠀⠀⠀⠀⠰⣦⣀⠙⢆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⢸⠀⢰⡏⢹⡇⠀⠀⣾⡿⠀⠸⡄⢸⣇⠀⠀⡏⣷⡀⠸⣷⣌⢣⡀⠀⠀⢹⣄⠈⢳⡀⠀⠀⠀⠸⣮⠓⣤⣻⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠧⠘⡄⣸⠀⢸⣷⠀⢰⡿⡧⡀⠀⢣⠈⣿⡀⠀⣷⢻⢣⠀⢹⣿⣦⡑⣄⠀⠀⢻⣆⠀⠹⣦⡀⠀⠀⢹⣏⠀⠙⣧⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡏⠀⠈⠻⡆⣸⣧⣷⠿⣆⠈⢆⢻⣷⡀⢹⣿⠀⠱⡄⢻⡷⡑⢮⣳⡀⠈⣿⣄⠀⢻⣏⠳⢄⡀⢻⣄⣴⣿⡃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠙⢿⣿⡷⠀⣿⣧⣼⢦⣿⣳⣄⣿⣧⠀⢈⣓⣷⣼⠮⣿⡿⢦⣽⣿⣧⠘⣿⣀⠠⣿⣾⣿⠋⠙⣧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠚⢻⡗⠀⠹⡿⢠⠀⠙⣮⠻⢿⡟⢿⣿⣩⣿⣿⠻⢾⠷⡀⢸⠻⣯⠳⣿⡟⢉⣻⣿⣧⠀⠀⢹
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢶⠟⠁⠀⢸⡇⠈⠉⠁⠀⠀⠀⠈⠷⠀⠈⠈⠹⢿⣿⠏⠀⠈⢳⣼⢾⡆⢿⣴⣿⡗⢫⠈⢻⢿⣷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣡⠏⠀⠀⠀⢸⡆⠀⢠⡖⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠀⠀⠠⠞⠁⠀⠁⠸⣧⡼⠇⠚⣠⠏⠈⠻⣷⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢉⡤⠠⣤⡀⠀⠳⣄⠈⠻⠄⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⡟⠁⠀⠀⢀⠈⠓
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⣸⡇⣼⠋⣷⢠⠀⠙⢦⠀⠀⠻⣿⡟⠁⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⢹⣿⢧⠀⠀⠀⠀⠉⠂
⠀⠀⠀⠀⠀⠀⠀⢀⣰⠏⠀⢿⣿⣷⡿⣃⣾⣤⣤⣼⣷⣄⠀⠹⠇⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠓⡌⡎⢢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠴⠋⠁⠀⠀⠀⠉⢩⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⢀⣤⣂⣤⣶⡿⠋⣀⣴⣿⣘⣆⠻⣦⡀⠀
⠀⠀⢀⠴⠊⠁⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠑⠒⠚⢁⣀⣠⠴⠾⣿⣿⠟⠋⠁⠀⢾⡿⠟⠋⠉⣯⠳⡘⢿⡦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡿⠟⢻⡏⣿⠀⠉⠻⣿⡿⠋⠉⠻⢄⠀⠛⠋⠀⠀⠀⠀⠀⢀⣠⠴⠛⠁⠀⠈⣷⢝
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⠟⠉⠀⠀⡜⣷⡏⢷⠀⢸⣿⣧⡀⠀⠀⠸⡇⠀⠀⠀⢀⡤⠒⠋⠁⠀⠀⣀⣠⣴⠾⢿⡄
⢀⡂⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⢻⢻⢸⠀⣼⠁⠈⠳⣦⠀⠀⣿⢻⡇⣴⠟⠀⢀⣠⣴⠾⠛⠋⠁⠀⠀⠀⢷
⠉⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠸⡆⢟⣳⡟⠀⢤⡀⠘⣧⠀⣿⢸⡾⠃⠀⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈
⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣼⣟⠁⠀⠀⠳⣄⠘⣧⣙⠛⢁⣠⡾⠃⠀⠀⣀⣠⠴⠚⠁⠘⠦⡀⠀
"""



TERMINAL_WIDTH = shutil.get_terminal_size().columns

#ẩn cursor terminal
sys.stdout.write("\033[?25l")

class Song:
    def __init__(self):
        global ASUKA
        """
        Setup biến cục bộ
        """
        #clear màn hình
        self.clrscr()

        #chơi nhạc nền
        
        self.timelapse = time.time()
        #intro 3 giây đầu (trước khi hát)
        print(" "*((TERMINAL_WIDTH-5)//2),end="")
        for i in range(3):
            print(self.interpolate_color((147, 5, 163), (16, 11, 230), i*(1/3), True) + "♪", end = " ")
            if (i==2):break
            time.sleep(1)
        time.sleep(0.5)
        print()
        self.clrscr()
        ASUKA = ASUKA.split("\n")
        for i in ASUKA:
            print(' '*((TERMINAL_WIDTH-len(ASUKA[0]))//2)+ i[0:])
            time.sleep(0.0001)
        self.music = ["♪", "♩", "♫"]
        #danh sách màu (không dùng)
        self.color_set = [
            [(147, 5, 163), (16, 11, 230)], 
            [(7, 186, 222), (0, 204, 48)],
            [(247, 247, 247), (186, 99, 11)]
        ]
        #lời bài hát (căn chỉnh thời gian chuyển đổi)
        self.data = [
            ("Đã lỡ yêu, lỡ yêu, yêu, yêu, yêu, yêu, yêu",3),
            ("Đã lỡ yêu, lỡ yêu, yêu, yêu, yêu, yêu, yêu",9),
            ("Đã lỡ yêu, lỡ yêu, yêu, yêu, yêu, yêu, yêu",15),
            ("Đã lỡ yêu, lỡ yêu, can you feel? Ah",21),
            ("Đã lỡ yêu em nhiều rồi thì anh chỉ biết ngắm mưa",25),
            ("Nhìn qua hàng cây được bao nhiêu hạt mưa",29),
            ("Là trong anh được bấy nhiêu nỗi nhớ",32),
            ("Đã lỡ yêu em nhiều rồi thì anh chỉ biết đếm sao",37),
            ("Nhìn lên trời cao được bao nhiêu vì sao",40),
            ("Là trong lòng anh còn bấy nhiêu những nỗi lo",43),
            ("Sợ mình đánh mất em khi thu vừa sang, lá xanh bỗng úa vàng",47),
            ("Khi mưa còn chưa tới, em thay người yêu mới, oh-no-oh-no",53),
            ("Sợ mình sẽ khiến em yêu phai nhạt hơn giữa mênh mông bộn bề",59),
            ("Em ơi, chờ anh với (chờ anh với)",65),
            ("Chỉ biết nói cho em nghe vậy thôi (no)",68),
            ("Vì đã lỡ yêu em rồi, chẳng dám hứa xa xôi",71),
            ("Cứ nhắm mắt em lại và feel my love (love)",77),
            ("Dù nắng mưa bao mùa thì tình anh vẫn luôn đây mà, chẳng phải kiếm đâu xa (xa)",81),
            ("Vẫn giữ đó bầu trời của riêng chúng ta (ta)",89),
            ("Để gió mang đi về một nơi không người (ah)",93),
            ("Đã lỡ yêu em nhiều rồi thì anh chỉ biết thế thôi (thế thôi)",97),
            ("Dù mai về sau mình không bên cạnh nhau",101),
            ("Dù tim mình đau khi biết em đã lỡ yêu người",104),
            ("Đã lỡ yêu em nhiều rồi thì anh sẽ bất chấp luôn (chấp luôn)",109),
            ("Dù mưa, dù giông, dù sông sâu, biển xa (xa)",113),
            ("Dù nắng cháy, anh cũng không hề lo",116),
            ("Chỉ sợ mình đánh mất em khi thu vừa sang, lá xanh bỗng úa vàng (oh-oh)",119),
            ("Khi mưa còn chưa tới (oh-no), em thay người yêu mới, oh-no, no",125),
            ("Sợ mình sẽ khiến em yêu phai nhạt hơn giữa mênh mông bộn bề",131),
            ("Em ơi, chờ anh với (chờ anh với)",137),
            ("Chỉ biết nói cho em nghe vậy thôi (chỉ biết nói), no",140),
            ("Vì đã lỡ yêu em rồi, chẳng dám hứa xa xôi",143),
            ("Cứ nhắm mắt em lại và feel my love (love)",149),
            ("Dù nắng mưa bao mùa thì tình anh vẫn luôn đây mà, chẳng phải kiếm đâu xa",153),
            ("Vẫn giữ đó bầu trời của riêng chúng ta",161),
            ("Để gió mang đi về một nơi không người",165),
            ("Đã lỡ yêu, nah-nah-nah (lỡ yêu)",168),
            ("You know, oh, lỡ yêu, nah-nah-nah (lỡ yêu)",170),
            ("I love you so, bae, I love you so",173),
            ("Mình phải bước chậm lại vì ngày mai rất dài",177),
            ("Đã lỡ yêu, nah-nah-nah (lỡ yêu)",180),
            ("You know, oh, lỡ yêu, nah-nah-nah (lỡ yêu)",182),
            ("I love you so, bae, I love you so",185),
            ("Mình phải bước chậm lại vì ngày mai rất dài (chậm lại, chậm lại)",189),
            ("Vì biết đâu sớm mai thức dậy",191),
            ("Em không còn đây ôm anh, nhẹ hôn anh, để tình ta cứ trôi lững lờ",194),
            ("Chờ giông và bão cuốn đi bất ngờ",201),
            ("Rồi lỡ đâu giấc mơ không thành",203),
            ("Em không còn kề vai anh, tình mong manh, một người đứng, cứ trông với chờ",207),
            ("Người kia thì ôm giấc mơ (giấc mơ)",212),
            ("Vì đã lỡ yêu em rồi, chẳng dám hứa xa xôi (chẳng dám hứa thêm gì nữa)",215),
            ("Cứ nhắm mắt em lại và feel my love (can you feel my love, love, bae?)",220),
            ("Dù nắng mưa bao mùa thì tình anh vẫn đây mà, chẳng phải kiếm đâu xa",225),
            ("Vẫn giữ đó bầu trời của riêng chúng ta (love you so, love you so)",233),
            ("(Love you so much) để gió mang đi về một nơi không người (I love you so)",237),
            ("Đã lỡ yêu, vì một người lỡ yêu, lỡ yêu (yêu, yêu, yêu, yêu, yêu)",240),
            ("♪ ♪ ♪...",250),
            ("", 261)
        ]
    
    def clrscr(self):
        """
        hàm xoá màn hình
        """
        return os.system("cls") if os.name == "nt" else os.system("clear")

    def random_color(self, dark: bool = False):
        """
        hàm lấy mã màu rgb
        """
        if dark:
            return random.choice([
                (255,random.randint(0,100),random.randint(0,100)),
                (random.randint(0,100),255,random.randint(0,100)),
                (random.randint(0,100),random.randint(0,100),255)
                ]
            )
        return random.choice([
                (0,random.randint(150,255),random.randint(150,255)),
                (random.randint(150,255),0,random.randint(150,255)),
                (random.randint(150,255),random.randint(150,255),0)
                ]
            )

    @staticmethod
    def play_song():
        """
        hàm chơi nhạc
        """
        winsound.PlaySound("song.wav",winsound.SND_ASYNC)

    def interpolate_color(self, c1: str, c2: str, factor: float, bool=False):
        """
        hàm tạo màu trung gian giữa 2 màu
        """
        r1,g1,b1=c1
        r2,g2,b2=c2
        r = int(r1 + (r2 - r1)*factor)
        g = int(g1 + (g2 - g1)*factor)
        b = int(b1 + (b2 - b1)*factor)
        if bool:
            return f"\033[1m\033[38;2;{r};{g};{b}m"
        return f"\033[38;2;{r};{g};{b}m"

    def get_color(self, rgb: tuple, bool: bool=False):
        r,b,g = rgb
        if bool:
            return f"\033[1m\033[38;2;{r};{g};{b}m"
        return f"\033[38;2;{r};{g};{b}m"

    def add_to_tuple(self, tup: tuple, num: int):
        """
        hàm tăng giá trị cho màu (mục đích làm tối màu, tạm thời k dùng đến)
        """
        return tuple(map(lambda x: x + num, tup))

    def brighten_rgb(self, color: tuple, factor: float=1.2):
        """
        hàm làm sáng màu
        """
        r, g, b = color
        r = min(int(r * factor), 255)
        g = min(int(g * factor), 255)
        b = min(int(b * factor), 255)
        return r, g, b

    def animation(self, content: str, slow: float, music_icons: bool = True, rgb: tuple = ()):
        """
        hàm chạy text theo nhạc
        """
        if music_icons:
            content = random.choice(self.music) + " " + content
        colored_list = []
        #lấy 2 mã màu bất kì , điều kiện từ sáng -> tối
        if not rgb:
            picked = [(self.random_color(dark=False)), self.random_color(dark=True)]
        else:
            picked = [(255,255,255), rgb]
        for i in range(len(content)):
            colored_list.append(
                self.interpolate_color(
                    picked[0], picked[1], i*(1/(len(content)))
                )
            )
        
        #thuật toán chạy 
        padding = (TERMINAL_WIDTH-len(content))//2
        space_left = TERMINAL_WIDTH - (padding + len(content)) - 1
        tmp = "\033[0m"
        for i in range(len(content)):
            tmp += colored_list[i] + content[i]
        print(" "*padding + tmp + " "*space_left, end="\r")
        for i in range(len(content)):
            anim_text = "\033[1m"
            colored_list = [colored_list[-1]] + colored_list[:-1]
            for j in range(len(content)):
                anim_text += colored_list[j] + content[j]
                if (j==i):
                    anim_text += "\033[0m"
            print(" "*padding + anim_text + " "*space_left, end="\r")
            time.sleep(slow)
        


    def play(self):
        """
        hàm chạy chính
        """
        for i in range(len(self.data)-1):
            text, timelapse = self.data[i]
            while (int(time.time()-self.timelapse) != timelapse):pass
            self.animation(
                text,
                abs(timelapse-self.data[i+1][1]+0.5)/len(text)
            )
        self.clrscr()
        credits = [
            ("♪ Credits ♪", (204,102,0)),
            ("♪ Made by Hngl", (255,128,0)),
            ("♪ Cam on moi nguoi da lang nghe!",(0,0,0)),
            ("♪ Thanks for listening everyone!",(0,0,0)),
            ("▷ Youtube : https://www.youtube.com/@rtech2808",(255,51,51)),
            ("ƒ Facebook : https://www.facebook.com/hngl2808",(102,102,255)),
        ]
        for i in range(len(credits)):
            text, rgb = credits[i]
            self.animation(
                content=text,
                slow=3/len(text),
                music_icons=False,
                rgb=rgb
            )
            print("")

if __name__ == "__main__":
    playsong = threading.Thread(target=Song.play_song).start
    try:
        playsong()
        obj = Song()
        obj.play()
    except KeyboardInterrupt:
        winsound.PlaySound(None, winsound.SND_PURGE)
        
    #hiển thị lại cursor terminal
    sys.stdout.write("\033[?25h")
