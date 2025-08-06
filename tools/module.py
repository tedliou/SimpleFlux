import json
import os

class Config:
    def __init__(self, path):
        self.path = path
        self.data = {
            "name": "",
            "version": "",
            "window_width": 0,
            "window_height": 0,
            "lux_path": "",
            "ffmpeg_path": "",
            "output_path": "",
        }
        self.is_new_file = self.load()
    
    # Load
    def load(self):
        file_exist = os.path.exists(self.path)
        is_new_file = True
        cfg = None
        
        if file_exist:
            try:
                with open(self.path, "r", encoding="utf-8") as file:
                    cfg = json.load(file)

                self.data = cfg
                is_new_file = False

            except json.JSONDecodeError as e:
                print(e.msg)
                is_new_file = True

            except Exception as e:
                print(e)
                is_new_file = True
        
        if is_new_file:
            self.save()

        return is_new_file
    
    
    # Save
    def save(self):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)
    
    # Name
    def set_name(self, name):
        self.data["name"] = name
        self.save()
    def get_name(self):
        return self.data["name"]
    
    # Version
    def set_version(self, version):
        self.data["version"] = version
        self.save()
    def get_version(self):
        return self.data["version"]
    
    # Window
    def set_window_width(self, width):
        self.data["window_width"] = width
        self.save()
    def get_window_width(self):
        return self.data["window_width"]
    def set_window_height(self, height):
        self.data["window_height"] = height
        self.save()
    def get_window_height(self):
        return self.data["window_height"]
    
    # Lux
    def set_lux_path(self, lux_path):
        self.data["lux_path"] = lux_path
        self.save()
    def get_lux_path(self):
        return self.data["lux_path"]
    
    # FFMPEG
    def set_ffmpeg_path(self, ffmpeg_path):
        self.data["ffmpeg_path"] = ffmpeg_path
        self.save()
    def get_ffmpeg_path(self):
        return self.data["ffmpeg_path"]
    
    # Output
    def set_output_path(self, output_path):
        self.data["output_path"] = output_path
        self.save()
    def get_output_path(self):
        return self.data["output_path"]
