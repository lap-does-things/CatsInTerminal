import requests, PIL, curses
from PIL import Image

def main():
    curses.initscr()
    curses.noecho()
    curses.cbreak()
    screen = curses.initscr()
    assert screen is not None
    Req = requests.get("https://api.thecatapi.com/v1/images/search?limit=1")
    # [x] АПИ следующего вида :
    """
    [
        {
        'id': 'MjA2Nzg5OQ',
        'url': 'https://cdn2.thecatapi.com/images/MjA2Nzg5OQ.jpg',
        'width': 500,
        'height': 333
        }
    ]
    """
    imgurl = Req.json()[0]['url']
#    img = PIL.Image.open(requests.get(imgurl, stream=True).raw).resize((int(os.get_terminal_size().columns/2), os.get_terminal_size().lines))
    img = PIL.Image.open(requests.get(imgurl, stream=True).raw).resize((170, 40))
    img = img.convert('L')
    px = img.load()
    curses.start_color()
    for i in range(0, img.size[0]):
        for j in range(0, img.size[1]):
            screen.addstr(j, i, " " if px[i, j] >= 220 else "." if px[i,j] > 200 else ":" if px[i,j] > 199 else ";" if px[i,j] > 171
                          else "+" if px[i,j] > 143 else "" if px[i,j] > 115 else "=" if px[i,j] > 87 else "x" if px[i,j] > 59 else "X"
                          if px[i,j] > 31 else "$") #█"

    screen.refresh()
    screen.getch()

main()