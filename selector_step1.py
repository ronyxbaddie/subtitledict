import tkinter as tk
import ctypes  # for Windows DPI
import pyautogui

class RegionSelector:
    def __init__(self):
        self.start_x = self.start_y = 0
        self.rect = None

        # DPI awareness for Windows
        ctypes.windll.user32.SetProcessDPIAware()

        # Get DPI scale factor
        self.screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        self.screen_height = ctypes.windll.user32.GetSystemMetrics(1)

        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg='black')
        self.root.config(cursor="crosshair")
        self.root.bind("<Escape>", lambda e: self.root.destroy())

        self.canvas = tk.Canvas(self.root, cursor="crosshair", bg="black", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

        # get logical screen size (as tkinter sees it)
        self.tk_width = self.root.winfo_screenwidth()
        self.tk_height = self.root.winfo_screenheight()

        # compute DPI scale
        self.scale_x = self.screen_width / self.tk_width
        self.scale_y = self.screen_height / self.tk_height

    def on_mouse_down(self, event):
        # For screen capture (DPI-scaled)
        self.start_x = int(event.x_root * self.scale_x)
        self.start_y = int(event.y_root * self.scale_y)

        # For drawing on canvas
        self.canvas_start_x = event.x
        self.canvas_start_y = event.y

        self.rect = self.canvas.create_rectangle(self.canvas_start_x, self.canvas_start_y,
                                                self.canvas_start_x, self.canvas_start_y,
                                                outline='white', fill='gray80', width=2)

    def on_mouse_drag(self, event):
        self.canvas.coords(self.rect,
                        self.canvas_start_x, self.canvas_start_y,
                        event.x, event.y)


    def on_mouse_up(self, event):
        end_x = int(event.x_root * self.scale_x)
        end_y = int(event.y_root * self.scale_y)

        bbox = (min(self.start_x, end_x), min(self.start_y, end_y),
                max(self.start_x, end_x), max(self.start_y, end_y))

        print(f"Selected region: {bbox}")
        self.root.destroy()
        self.bbox = bbox

    def get_bbox(self):
        self.root.mainloop()
        return getattr(self, 'bbox', None)
