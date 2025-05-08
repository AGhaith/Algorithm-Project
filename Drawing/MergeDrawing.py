import Utilities.Global_Variables as gv

def MegreDrawing(color_array=None):
    gv.canvas.delete("all")

    box_width = 50
    box_height = 30
    box_offset = 10
    arr = gv.MERGE_ARRAY

    total_width = len(arr) * (box_width + box_offset) - box_offset
    start_x = (gv.CANVAS_WIDTH - total_width) / 2

    for i, val in enumerate(arr):
        x0 = start_x + i * (box_width + box_offset)
        y0 = 20
        x1 = x0 + box_width
        y1 = y0 + box_height

        color = color_array[i] if color_array is not None else "lightblue"

        gv.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        gv.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(val), anchor="center", font=("Arial", 10))

    gv.canvas.update_idletasks()
    gv.canvas.after(50)
