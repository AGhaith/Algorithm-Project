import Utilities.Global_Variables as gv

def draw_array(color_array=None):
    gv.canvas.delete("all")
    bar_width = gv.CANVAS_WIDTH / gv.LENGTH_OF_ARRAY
    arr = gv.arr
    max_val = max(arr)

    # Ensure max_val is not zero to prevent division by zero
    if max_val == 0:
        max_val = 1  # Prevent division by zero if max is 0

    # Set the offset for leaving space at the bottom for the text
    bar_offset = 30  # Amount to move the bars up

    for i, val in enumerate(arr):
        x0 = i * bar_width

        # Adjust the bar height to leave room for the text
        # Scale the height based on the canvas height and max value, ensuring no bars go below the offset
        scaled_height = (val / max_val) * (gv.CANVAS_HEIGHT - bar_offset)

        # Ensure that the bar height is at least a small value (like 1px) so it doesn't disappear for small values
        if scaled_height < 1:
            scaled_height = 1  # Minimum height to avoid disappearing bars

        # Calculate y0 to position the bar correctly
        y0 = gv.CANVAS_HEIGHT - scaled_height - bar_offset

        # Bottom of the bar is offset from the canvas
        x1 = (i + 1) * bar_width
        y1 = gv.CANVAS_HEIGHT - bar_offset  # Bottom of the bar, just above the canvas bottom

        # Color handling
        color = color_array[i] if color_array is not None else "blue"

        # Draw bar with outline
        gv.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

        # Draw value below the bar (make sure it stays within canvas)
        text_y = y1 + 10  # Adjust text position just below the bar
        if text_y > gv.CANVAS_HEIGHT - 10:
            text_y = gv.CANVAS_HEIGHT - 10  # Ensure text doesn't go out of bounds

        gv.canvas.create_text((x0 + x1) / 2, text_y, text=str(val), anchor="n", font=("Arial", 10))

    # gv.time.sleep(0.05)  # Uncomment if you want a small delay
    gv.canvas.update_idletasks()
