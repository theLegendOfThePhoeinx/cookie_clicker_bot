import pyautogui as pg
import keyboard as key


class Bot:

    # list if all the different things inteh cookie clicker store
    IMAGES_LIST = ['Idleverse.png', 'Javascript Consol.png', 'Fractal Engine.png', 'Chancmaker.png', 'Prism.png', 'Antim. Condenser.png', 'Time machine.png', 'Portal.png', 'Alchemy Lab.png', 'Shipment.png', 'Wizard Tower.png', 'Temple.png', 'Bank.png', 'Factory.png', 'Mine.png', 'Farm.png', 'Grandma.png', 'Cursor.png']
    # list of all the folders containing the screen shots
    SCREENSHOTS_FOLDER = 'Screenshots'
    KNOWN_UNAVAILABLE_FOLDER = 'Known Unavailabe'
    UNKNOWN_FOLDER = 'Unknown Screenshots'

    def __init__(self, cookie_coords: tuple, store_x):
        self.cookie_coords = cookie_coords
        self.imgs = self.IMAGES_LIST
        self.screenshots_folder = self.SCREENSHOTS_FOLDER
        self.known_unavailable_folder = self.KNOWN_UNAVAILABLE_FOLDER
        self.unknown_folder = self.UNKNOWN_FOLDER
        self.store_x = store_x

    def click_cookie(self):
        x = self.cookie_coords[0]
        y = self.cookie_coords[1]
        pg.click(x, y)

    def scroll_store_up(self, scroll_distance):
        pg.moveTo(self.store_x, 1000)
        pg.scroll(scroll_distance)

    def scroll_store_down(self, scroll_distance):
        pg.moveTo(self.store_x, 1000)
        pg.scroll(-scroll_distance)

    def scroll_top_half_store(self, scroll_distance=1000):
        self.scroll_store_up(scroll_distance)

    def scroll_bottom_half_store(self, scroll_distance=1000):
        self.scroll_store_up(scroll_distance)

    def find_things(self):
        if key.is_pressed("e"):
            exit()

        pg.
        self.scroll_store_down(1000)
        scroll_count = 0
        for image in self.imgs:
            path_available = self.screenshots_folder + '/' + image
            print(path_available)
            img_location = pg.locateCenterOnScreen(path_available)
            print(image)
            print(img_location)

            if img_location is not None:
                pg.click(img_location[0], img_location[1])


            else:
                tries = 0

                while img_location is None and tries <= 10:
                    if scroll_count <= 5:
                        self.scroll_store_up(200)
                        scroll_count += 1

                    elif scroll_count > 5 or scroll_count <= 10:
                        self.scroll_store_down(200)
                        scroll_count += 1

                    if scroll_count == 10:
                        scroll_count = 0

                    img_location = pg.locateCenterOnScreen(path_available)

                    if img_location is not None:
                        tries = 10


                    if key.is_pressed("e"):
                        exit()

                    tries += 1

            if img_location is not None:
                pg.click(img_location[0], img_location[1])

            if key.is_pressed("e"):
                        exit()

            


if __name__ == '1':
    bot = Bot(cookie_coords=(273, 472), store_x=1770)
    while True:
        bot.click_cookie()
        bot.find_things()
    