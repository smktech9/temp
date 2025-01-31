from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.resize import resize
import os

def split_video(input_path, output_dir, clip_duration=6, width=360, height=240):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Load the video
    video = VideoFileClip(input_path)
    total_duration = video.duration

    # Iterate over the video duration and save clips
    for start_time in range(0, int(total_duration), clip_duration):
        end_time = min(start_time + clip_duration, total_duration)
        clip = video.subclip(start_time, end_time)
        resized_clip = resize(clip, height=height, width=width)
        
        output_path = os.path.join(output_dir, f"clip7_{start_time}-{end_time}.mp4")
        resized_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Saved: {output_path}")

    # Close the video file
    video.close()
    print("Video splitting completed.")

# Example usage
input_video_path = "/home/shivansh/Music/workspace/video7.webm"
output_directory = "/home/shivansh/Music/workspace"
split_video(input_video_path, output_directory)

