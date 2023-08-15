import os
import curses
from libsixel.encoder import Encoder, SIXEL_OPTFLAG_WIDTH, SIXEL_OPTFLAG_COLORS

TERMINAL_WIDTH = os.get_terminal_size().columns
def show_image(filename):
    encoder = Encoder()
    encoder.setopt(SIXEL_OPTFLAG_WIDTH,TERMINAL_WIDTH*10 )
    encoder.setopt(SIXEL_OPTFLAG_COLORS, "16")
    encoder.encode(filename)


def show(stdscr, file):
    stdscr.clear()
    show_image(file)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    curses.noecho()
    curses.cbreak()

    stdscr.clear()
    current_directory = os.getcwd()
    png_files = [file for file in os.listdir(
        current_directory) if file.endswith('.png') or file.endswith(".jpg")]
    current_index = 0

    while True:
        #    stdscr.clear()
        stdscr.addstr( os.get_terminal_size().lines-1,0
, "Press 'Q' to quit")

        if png_files:
            filename = png_files[current_index]
            stdscr.addstr( os.get_terminal_size().lines-2,0, f"Showing: {filename}", curses.A_BOLD)
            show_image(filename)
        else:
            stdscr.addstr(1, 0, "No .png files found in the directory.")
        # show_image(png_files[current_index])
        # stdscr.refresh()

        key = stdscr.getch()

        if key == ord('q') or key == ord('Q'):
            break
        elif key == curses.KEY_RIGHT:
            # stdscr.clear()
            # stdscr.refresh()
            stdscr.clear()
            stdscr.refresh()

            current_index = (current_index + 1) % len(png_files)
        elif key == curses.KEY_LEFT:
            # stdscr.clear()
            # stdscr.refresh()
            stdscr.clear()
            stdscr.refresh()

            current_index = (current_index - 1) % len(png_files)


if __name__ == "__main__":
    curses.wrapper(main)
