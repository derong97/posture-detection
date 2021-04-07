import seeed_mlx9064x
import time
import numpy as np
import os
import glob


CHIP_TYPE = 'MLX90640'
save_filepath = "/home/pi/Desktop/posture-data/stand/"

def take_ten_frames(mlx, frame):
    frames = np.array([])

    for i in range (0,10):
        try:
            mlx.getFrame(frame)
        except ValueError:
            continue
        print(frame)
        frame = np.array(frame)
        if i == 0:
            frames = frame
        else:
            # frame_formatted = np.reshape(frame,(24, 32)) 
            frames = np.vstack((frames, frame))
        print("frame", (i + 1), " captured")
        
    
    return frames 


def save_ten_frames(frames, save_filepath):
    print(frames)
    current_files= os.listdir(save_filepath)

    if len(current_files) == 0:
        save_filepath = save_filepath + "stand_001"
        np.save(save_filepath, frames)
    else: #get number of files 
        save_index = len(current_files) 
        if save_index < 9: 
            save_filepath = save_filepath + "stand_00" + str(save_index+1)
        elif save_filepath < 99: 
            save_filepath = save_filepath + "stand_0" + str(save_index+1)
        else: 
            save_filepath = save_filepath + "stand_" + str(save_index+1)
        
        np.save(save_filepath, frames)
    
    print (save_filepath, "saved")

def main():

    if CHIP_TYPE == 'MLX90641':
        mlx = seeed_mlx9064x.grove_mxl90641()
        frame = [0] * 192
    elif CHIP_TYPE == 'MLX90640':
        mlx = seeed_mlx9064x.grove_mxl90640()
        frame = [0] * 768       
    
    while True:
        try:
            frames = take_ten_frames(mlx, frame)
            save_ten_frames(frames, save_filepath)

        except KeyboardInterrupt:
            break
            
if __name__  == '__main__':
    main()
