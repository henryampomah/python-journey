# %%
import random
def list_of_hexa_colors():
    hexa_colors = []
    for _ in range(3):
        color = '#'
        for _ in range(6):
            color += random.choice('0123456789ABCDEF')
        hexa_colors.append(color)
        
    return hexa_colors
list_of_hexa_colors()

# %%
def list_of_rgb_colors():
    rgb_colors = []
    for _ in range(3):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r}, {g}, {b})")
    return rgb_colors
list_of_rgb_colors()
# %%
def generate_colors(color_type, num_colors):
    colors = []
    if color_type == 'hexa':
        for _ in range(num_colors):
            color = '#'
            for _ in range(6):
                color += random.choice('0123456789ABCDEF')
            colors.append(color)
    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f"rgb({r}, {g}, {b})")
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
    return colors
generate_colors('hexa', 5)
# generate_colors('rgb', 5)
# %%
