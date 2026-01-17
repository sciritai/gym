from moviepy import VideoFileClip

input_video = "loki_gym_video.mp4"

# (Start Time, Duration, Filename)
clips_to_make = [
    (10, 5, "01_seated_chest_press.gif"),
    (27, 5, "02_incline_press.gif"),
    (44, 5, "03_decline_press.gif"),
    (60, 5, "04_chest_fly.gif"),
    (77, 5, "05_shoulder_press.gif"),
    (94, 5, "06_lateral_raise.gif"),
    (110, 5, "07_front_raise.gif"),
    (127, 5, "08_lat_pulldown.gif"),
    (144, 5, "09_seated_row.gif"),
    (160, 5, "10_bent_over_row.gif"),
    (177, 5, "11_face_pull.gif"),
    (194, 5, "12_bicep_curl.gif"),
    (210, 5, "13_tricep_pushdown.gif"),
    (227, 5, "14_overhead_tricep_ext.gif"),
    (244, 5, "15_leg_extension.gif"),
    (260, 5, "16_leg_curl.gif"),
    (277, 5, "17_leg_press.gif"),
    (310, 5, "18_squat.gif"),
    (327, 5, "19_weighted_lunge.gif"),
    (344, 5, "20_ab_crunch.gif"),
    (360, 5, "21_woodchopper.gif")
]

def make_gym_gifs(file_path, segments):
    with VideoFileClip(file_path) as video:
        for start, duration, name in segments:
            print(f"Processing: {name}...")
            
            # Use 'subclipped' and 'resized' for MoviePy 2.0+
            clip = (video.subclipped(start, start + duration)
                         .resized(width=480))
            
            # Cleanest call: only passing name and fps
            # MoviePy 2.0 handles the optimization automatically now
            clip.write_gif(name, fps=15)
            
            clip.close()
    print("--- Done! All GIFs generated. ---")

if __name__ == "__main__":
    make_gym_gifs(input_video, clips_to_make)