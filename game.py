"""
From Arcade Array Backed Grid Template
"""
import arcade
from game_logic import minesweeper_game

# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "MineSweeper - ENTER: Restart - ESC: Quit"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Set up the application.
        """

        super().__init__(width, height, title)

        self.game = minesweeper_game(ROW_COUNT, COLUMN_COUNT, 20)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(self.game.y):
            for column in range(self.game.x):
                # Figure out what color to draw the box
                square = self.game.board.grid[row][column]
                if square.isreveal is True:
                    color = arcade.color.WHITE
                    if square.isbomb is True:
                        color = arcade.color.RED
                else:
                    if square.ismarked is True:
                        color = arcade.color.DARK_TURQUOISE
                    else:
                        color = arcade.color.COOL_GREY

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

                #Draw the text
                if (
                    square.counter > 0
                    and square.isbomb is False
                    and square.isreveal is True
                ):
                    if square.counter == 1:
                        color = arcade.color.BLUE
                    elif square.counter == 2:
                        color = arcade.color.GREEN
                    elif square.counter > 2:
                        color = arcade.color.RED

                    arcade.draw_text(
                        str(square.counter), x, y, color, font_size=15, bold=True
                    )

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < self.game.y and column < self.game.x:

            # Flip the location between 1 and 0.
            case = self.game.board.grid[row][column]
            if button == arcade.MOUSE_BUTTON_LEFT:
                if case.isreveal is False:
                    case.isreveal = True
                    if case.isbomb is True:
                        print("You lose. Press Enter to restart")
                    else:
                        self.game.reveal_count += -1
                        counter = self.game.board.reveal(case)
                        self.game.reveal_count += -counter
                        print(self.game.reveal_count)

                        if self.game.reveal_count == 0:
                            print("You win")
            elif button == arcade.MOUSE_BUTTON_RIGHT:
                case.mark()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.ENTER:
            print("Restart")
            self.game = minesweeper_game(ROW_COUNT, COLUMN_COUNT, 20)
        elif key == arcade.key.ESCAPE:
            exit()


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
