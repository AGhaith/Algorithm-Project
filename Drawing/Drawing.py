import Utilities.Global_Variables as gv

def draw_array(color_array=None):
    gv.canvas.delete("all")
    bar_width = gv.CANVAS_WIDTH / gv.LENGTH_OF_ARRAY
    arr = gv.arr
    max_val = max(arr)

    # Ensure max_val is not zero to prevent division by zero
    if max_val == 0:
        max_val = 1
    bar_offset = 30

    for i, val in enumerate(arr):
        x0 = i * bar_width

        scaled_height = (val / max_val) * (gv.CANVAS_HEIGHT - bar_offset)

        if scaled_height < 1:
            scaled_height = 1

        y0 = gv.CANVAS_HEIGHT - scaled_height - bar_offset

        x1 = (i + 1) * bar_width
        y1 = gv.CANVAS_HEIGHT - bar_offset

        color = color_array[i] if color_array is not None else "blue"

        gv.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

        text_y = y1 + 10
        if text_y > gv.CANVAS_HEIGHT - 10:
            text_y = gv.CANVAS_HEIGHT - 10

        gv.canvas.create_text((x0 + x1) / 2, text_y, text=str(val), anchor="n", font=("Arial", 10))

    gv.canvas.update_idletasks()
