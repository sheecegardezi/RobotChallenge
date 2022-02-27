import tkinter as tk
import time


class GUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Robot Challenge")
        self.grid_size = 5
        self.scale = 100
        self.width, self.height = self.grid_size * self.scale, self.grid_size * self.scale

        self.tabletop = tk.Canvas(self, width=self.width, height=self.height,
                                  bg="white", bd=1, confine=False, cursor="dot",
                                  relief="flat", scrollregion=(0, 0, self.width, self.height))

        # draw grid
        for i in range(self.grid_size):
            # Create line with coordinates x1,y1,...,xn,yn.
            self.tabletop.create_line(0, i * self.scale, self.width, i * self.scale)
            self.tabletop.create_line(i * self.scale, 0, i * self.scale, self.height)

        # draw robot
        # Create rectangle with coordinates x1,y1,x2,y2.
        self.robot = self.tabletop.create_rectangle(0, 0, self.scale, self.scale, fill="red")
        self.tabletop.pack()
        self.bind("<Key>", self.move_robot)

        self.tabletop.pack(fill="both", expand=True)
        self.tabletop.focus_set()
        self.tabletop.bind("<Key>", self.move_robot)
        self.bind("<Key>", self.move_robot)

    def mimic_move_robot(self, event):
        time.sleep(1)
        if event == "Left":
            # <KeyPress event state=Mod2 keysym=Left keycode=113 x=463 y=165>
            event = tk.Event()
            event.keycode = "113"
            event.keysym = "Left"
            event.char = "Left"
            event.state = "Mod2"
            event.type = "KeyPress"
            event.delta = 0
            self.move_robot(event)
            self.move_robot(event)

        elif event == "Right":
            # <KeyPress event state=Mod2 keysym=Right keycode=114 x=338 y=151>
            event = tk.Event()
            event.keycode = "114"
            event.keysym = "Right"
            event.char = "Right"
            event.state = "Mod2"
            event.type = "KeyPress"
            event.delta = 0
            self.move_robot(event)
            self.move_robot(event)

        elif event == "Up":
            event = tk.Event()
            event.keycode = "111"
            event.keysym = "Up"
            event.char = "Up"
            event.state = "Mod2"
            event.type = "KeyPress"
            event.delta = 0
            self.move_robot(event)
            self.move_robot(event)

        elif event == "Down":
            event = tk.Event()
            event.keycode = "116"
            event.keysym = "Down"
            event.char = "Down"
            event.state = "Mod2"
            event.type = "KeyPress"
            event.delta = 0
            self.move_robot(event)
            self.move_robot(event)

    def move_robot(self, event):

        if event.keysym == "Left":
            self.tabletop.move(self.robot, -self.scale / 2, 0)
        elif event.keysym == "Right":
            self.tabletop.move(self.robot, self.scale / 2, 0)
        elif event.keysym == "Up":
            self.tabletop.move(self.robot, 0, -self.scale / 2)
        elif event.keysym == "Down":
            self.tabletop.move(self.robot, 0, self.scale / 2)

    def task(self):
        self.mimic_move_robot("Down")
        self.mimic_move_robot("Right")
        self.mimic_move_robot("Right")
        self.mimic_move_robot("Up")
        self.mimic_move_robot("Left")


if __name__ == '__main__':
    gui = GUI()
    gui.after(1000, gui.task)
    gui.after(2000, gui.task)
    gui.mainloop()
