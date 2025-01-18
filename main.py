import pygame
import random

# initialize pygame
pygame.init()

japanese_characters = [
    "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", 
    "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は", "ひ", "ふ", "へ", "ほ", 
    "ま", "み", "む", "め", "も", "や", "ゆ", "よ", "ら", "り", "る", "れ", "ろ", "わ", "を", 
    "ん", "ぁ", "あ", "ぃ", "い", "ぅ", "う", "ぇ", "え", "ぉ", "お", "か", "が", "き", "ぎ", 
    "く", "ぐ", "け", "げ", "こ", "ご", "さ", "ざ", "し", "じ", "す", "ず", "せ", "ぜ", "そ", 
    "ぞ", "た", "だ", "ち", "ぢ", "っ", "つ", "づ", "て", "で", "と", "ど", "な", "に", "ぬ", 
    "ね", "の", "は", "ば", "ぱ", "ひ", "び", "ぴ", "ふ", "ぶ", "ぷ", "へ", "べ", "ぺ", "ほ", 
    "ぼ", "ぽ", "ま", "み", "む", "め", "も", "ゃ", "や", "ゅ", "ゆ", "ょ", "よ", "ら", "り", 
    "る", "れ", "ろ", "ゎ", "わ", "ゐ", "ゑ", "を", "ん", "ゔ", "ゕ", "ゖ", "ゝ", "ゞ", "ァ", 
    "ア", "ィ", "イ", "ゥ", "ウ", "ェ", "エ", "ォ", "オ", "カ", "ガ", "キ", "ギ", "ク", "グ", 
    "ケ", "ゲ", "コ", "ゴ", "サ", "ザ", "シ", "ジ", "ス", "ズ", "セ", "ゼ", "ソ", "ゾ", "タ", 
    "ダ", "チ", "ヂ", "ッ", "ツ", "ヅ", "テ", "デ", "ト", "ド", "ナ", "ニ", "ヌ", "ネ", "ノ", 
    "ハ", "バ", "パ", "ヒ", "ビ", "ピ", "フ", "ブ", "プ", "ヘ", "ベ", "ペ", "ホ", "ボ", "ポ", 
    "マ", "ミ", "ム", "メ", "モ", "ャ", "ヤ", "ュ", "ユ", "ョ", "ヨ", "ラ", "リ", "ル", "レ", 
    "ロ", "ヮ", "ワ", "ヰ", "ヱ", "ヲ", "ン", "ヴ", "ヵ", "ヶ", "ヷ", "ヸ", "ヹ", "ヺ", "･", 
    "ｦ", "ｧ", "ｨ", "ｩ", "ｪ", "ｫ", "ｬ", "ｭ", "ｮ", "ｯ", "ｰ", "ｱ", "ｲ", "ｳ", "ｴ", "ｵ", "ｶ", 
    "ｷ", "ｸ", "ｹ", "ｺ", "ｻ", "ｼ", "ｽ", "ｾ", "ｿ", "ﾀ", "ﾁ", "ﾂ", "ﾃ", "ﾄ", "ﾅ", "ﾆ", "ﾇ", 
    "ﾈ", "ﾉ", "ﾊ", "ﾋ", "ﾌ", "ﾍ", "ﾎ", "ﾏ", "ﾐ", "ﾑ", "ﾒ", "ﾓ", "ﾔ", "ﾕ", "ﾖ", "ﾗ", "ﾘ", 
    "ﾙ", "ﾚ", "ﾛ", "ﾜ", "ﾝ"
]

# variables
background_colour = (0, 0, 0) 
character_color = (42, 217, 42)
caption = pygame.display.set_caption("digital raining" ) 
display_size = (800, 600)

# window icon
pygame.display.set_icon(pygame.image.load("assets/matrix_icon.png"))

fps = 25
font = pygame.font.Font('assets/Noto Sans CJK Regular.otf', 22)
screen = pygame.display.set_mode(display_size) 


num_columns = 25
column_width = display_size[0] // num_columns

# Initialize positions and characters for each column 
columns = [{      'y_positions': [random.randint(-display_size[1], 0)],
    'characters': [random.choice(japanese_characters)],
    'trail_characters': [[random.choice(japanese_characters) for _ in range(10)]]   
            } for _ in range(num_columns)]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)

    for i in range(num_columns):
        # Update y_positions and add new random characters to the top of the column
        columns[i]['y_positions'] = [y + 5 for y in columns[i]['y_positions']] 
        if random.random() < 0.5 and (not columns[i]['y_positions'] or columns[i]['y_positions'][0] > 275):
            columns[i]['y_positions'].insert(0, -50)
            columns[i]['characters'].insert(0, random.choice(japanese_characters))
            columns[i]['trail_characters'].insert(0, [random.choice(japanese_characters) for _ in range(10)])  
        # Render characters and their trails with a color that fades as they fall down 
        for y, char, trail_chars in zip(columns[i]['y_positions'], columns[i]['characters'], columns[i]['trail_characters']):
           for k in range(1, 50):
            if k-1 < len(trail_chars):
             screen.blit(font.render(trail_chars[k-1], True, (0, max(0, 255 - k * 20), 0)), (i * column_width, y - k * 25))
           if 0 <= y <= display_size[1]:
            screen.blit(font.render(char, True, character_color), (i * column_width, y))

        # Remove characters that have fallen off the screen by using a dictionary comprehension and slicing
        columns[i] = {k: v[:len(columns[i]['y_positions'])] for k, v in columns[i].items()}

    pygame.display.flip()
    clock.tick(fps)

pygame.quit() 