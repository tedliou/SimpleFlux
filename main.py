# Import Config Tools
from tools.module import Config

# GUI & Basic Tools
import tkinter as tk
import subprocess
import os
import sys
import threading
from datetime import datetime


# Get config.json
def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))

base_dir = get_base_dir()
cfg = Config(path=f"{base_dir}\config.json")

# If config.json not exist, create a new one
if cfg.is_new_file:
    cfg.set_name("SimpleLux")
    cfg.set_version("1.0.0")
    cfg.set_window_width(600)
    cfg.set_window_height(250)
    cfg.set_lux_path("lux.exe")
    cfg.set_ffmpeg_path("ffmpeg")
    cfg.set_output_path("outputs")


# Download & Convert
def lux(url, type):
    lux_file_path = cfg.get_lux_path()
    lux_full_path = os.path.join(base_dir, lux_file_path)
    print(f"Lux Path: {lux_full_path}")

    output_folder_path = cfg.get_output_path()
    output_folder_full_path = os.path.join(base_dir, output_folder_path)
    print(f"Output Folder Path: {output_folder_full_path}")

    output_file_name = f"output_{int(datetime.now().timestamp())}"

    # Create output folder
    if os.path.exists(output_folder_full_path) is False:
        os.mkdir(output_folder_full_path)

    # Run Lux
    lux_command = f"{lux_full_path} -o {output_folder_full_path} -O {output_file_name} {url}"
    print(f"Process Command: {lux_command}")
    lux_process = subprocess.Popen(["start", "/wait", "cmd", "/c", lux_command], shell=True)
    lux_process.wait()

    # Video / Music Convert, and show the output file in explorer
    if type == 0:
        subprocess.Popen(["explorer", "/select,", os.path.join(output_folder_full_path, f"{output_file_name}.mp4")])
    elif type == 1:
        video_path = os.path.join(base_dir, output_folder_path, f"{output_file_name}.mp4")
        music_path = os.path.join(base_dir, output_folder_path, f"{output_file_name}.mp3")
        ffmpeg_command = f"ffmpeg -i {video_path} {music_path}"
        ffmpeg_command = subprocess.Popen(["start", "/wait", "cmd", "/c", ffmpeg_command], shell=True)
        ffmpeg_command.wait()
        os.remove(f"{output_folder_full_path}/{output_file_name}.mp4")
        subprocess.Popen(["explorer", "/select,", os.path.join(output_folder_full_path, f"{output_file_name}.mp3")])

# Create a new thread to run Lux / FFMPEG
def download(url, type):
    task = threading.Thread(target=lambda: lux(url=url, type=type))
    task.start()


# GUI
def main():
    # TK Init
    name = cfg.get_name()
    root = tk.Tk()
    root.title(name)

    # Window Settings
    width = cfg.get_window_width()
    height = cfg.get_window_height()
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    left = int((window_width - width)/2)
    top = int((window_height - height)/2)
    root.geometry(f"{width}x{height}+{left}+{top}")
    root.resizable(False, False)

    # Title
    title_text = tk.Label(root, text=name)
    title_text.pack()

    # Version
    version = cfg.get_version()
    version_text = tk.Label(root, text=version)
    version_text.pack()

    # Media Type
    type_val = tk.IntVar()

    # Video
    video_type = tk.Radiobutton(root, text="Video", variable=type_val, value=0)
    video_type.pack()
    video_type.select()
    
    # Music
    music_type = tk.Radiobutton(root, text="Music", variable=type_val, value=1)
    music_type.pack()

    # Input Field
    input_field = tk.Entry(root, width=50)
    input_field.pack(padx=20, pady=20)

    # Button
    download_button = tk.Button(root, text="Download", command=lambda: download(url=input_field.get(), type=type_val.get()))
    download_button.pack(padx=20, pady=20)

    root.mainloop()

# Main
if __name__ == "__main__":
    main()
