import Utilities.Global_Variables as gv
import tkinter as tk 
def MergeDrawing(array, level, x_start):
    box_width = 50
    box_height = 30
    box_offset = 10
    vertical_offset = 50

    
    start_x = x_start * (box_width + box_offset + 50) + 100
    y0 = level * vertical_offset

    for i, val in enumerate(array):
        x0 = start_x + i * (box_width + box_offset) + 50 
        y1 = y0 + box_height
        x1 = x0 + box_width 

        gv.canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue", outline="black")
        gv.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(val), anchor="center", font=("Arial", 10))

    gv.canvas.update_idletasks()
    gv.time.sleep(0.5)

