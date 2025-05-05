import Utilities.Global_Variables as gv

def draw_array(color_array=None):
    gv.canvas.delete("all")
    bar_width = gv.CANVAS_WIDTH / gv.LENGTH_OF_ARRAY
    arr = gv.arr
    max_val = max(arr)

    # Set the offset for leaving space at the bottom for the text
    bar_offset = 30  # Amount to move the bars up

    for i, val in enumerate(arr):
        x0 = i * bar_width
        # Adjust the bar height to leave room for the text
        y0 = gv.CANVAS_HEIGHT - (val / max_val * (gv.CANVAS_HEIGHT - bar_offset))
        x1 = (i + 1) * bar_width
        y1 = gv.CANVAS_HEIGHT - bar_offset  # Ensure the bar doesn't reach the very bottom
        color = color_array[i] if color_array is not None else "blue"

        # Draw bar with outline
        gv.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

        # Draw value below the bar (make sure it stays within canvas)
        text_y = y1 + 10  # Adjust text position just below the bar
        if text_y > gv.CANVAS_HEIGHT - 10:
            text_y = gv.CANVAS_HEIGHT - 10  # Ensure text doesn't go out of bounds

        gv.canvas.create_text((x0 + x1) / 2, text_y, text=str(val), anchor="n", font=("Arial", 10))

    gv.time.sleep(0.05)
    gv.canvas.update_idletasks()
