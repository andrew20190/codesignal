import numpy as np 

def boxBlur(image):
    np_image = np.array(image)

    image_width = len(image[0])
    image_height = len(image)
    box_width = 3
    box_height = 3

    blurred = []

    for top in range(0, image_height - box_height + 1):
        
        blurred.append([])

        for left in range(0, image_width - box_width + 1):
            
            print(top, left)
        
            box = np_image[top : top + box_height, left : left + box_width]
            box_mean = int(box.mean())
            
            blurred[top].append(box_mean)
    
    return blurred
