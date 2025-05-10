while((j>=0) and (key<arr[j])):
                color_array = ["red" if x == j or x == key else "blue" for x in range(length)]
                draw.draw_array(color_array)
                arr[j+1]=arr[j]
                j -=1
                arr[j+1]=key
            Global_Variables.NUMBER_OF_OPERATIONS += 1