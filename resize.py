import cv2
import os

def change_video_resolution(input_path, output_path, width, height):
    # Open the input video
    cap = cv2.VideoCapture(input_path)
    
    # Get the original video's FPS
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'XVID' for .avi, 'mp4v' for .mp4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if the video ends

        # Resize the frame
        resized_frame = cv2.resize(frame, (width, height))

        # Write the resized frame
        out.write(resized_frame)

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video saved at {output_path}")

def resize_videos_in_folder(input_folder, output_folder, width, height):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get all video files in the folder
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv', '.flv')
    videos = [f for f in os.listdir(input_folder) if f.lower().endswith(video_extensions)]

    if not videos:
        print("No videos found in the folder.")
        return

    for video in videos:
        input_path = os.path.join(input_folder, video)
        output_path = os.path.join(output_folder, f"resized_{video}")

        print(f"Resizing {video}...")
        change_video_resolution(input_path, output_path, width, height)

    print("All videos have been resized successfully.")

# Example usage
input_folder = "videos"  # Folder containing input videos
output_folder = "resized_videos"  # Folder to save resized videos
new_width = 320  # Desired width
new_height = 240  # Desired height

resize_videos_in_folder(input_folder, output_folder, new_width, new_height)

