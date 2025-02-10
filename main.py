import cv2
import os
from glob import glob

def extract_frames(video_path, num_frames):
    """
    Extract frames from video at equal intervals
    
    Args:
        video_path (str): Path to the video file
        num_frames (int): Number of frames to extract
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    # Get total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate the interval between frames
    interval = total_frames // (num_frames - 1) if num_frames > 1 else total_frames
    
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    
    frame_positions = range(0, total_frames, interval)[:num_frames]
    
    for idx, frame_pos in enumerate(frame_positions):
        # Set the frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_pos)
        
        # Read the frame
        ret, frame = cap.read()
        
        if ret:
            # Save the frame
            output_path = os.path.join('images', f'frame_{idx+1}.jpg')
            cv2.imwrite(output_path, frame)
            print(f'Saved frame {idx+1} of {num_frames}')
        else:
            print(f'Failed to extract frame {idx+1}')
    
    # Release the video capture object
    cap.release()

def main():
    # Get list of videos in the video directory
    video_files = glob('video/*')
    
    if not video_files:
        print("No video files found in the 'video' directory!")
        return
    
    # Print available videos
    print("\nAvailable videos:")
    for idx, video in enumerate(video_files, 1):
        print(f"{idx}. {os.path.basename(video)}")
    
    # Get user input for video selection
    while True:
        try:
            choice = int(input("\nSelect video number: ")) - 1
            if 0 <= choice < len(video_files):
                selected_video = video_files[choice]
                break
            print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get number of frames from user
    while True:
        try:
            num_frames = int(input("\nHow many frames do you want to extract? "))
            if num_frames > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Process the video
    print(f"\nProcessing video: {os.path.basename(selected_video)}")
    extract_frames(selected_video, num_frames)
    print("\nFrame extraction completed!")

if __name__ == "__main__":
    main() 