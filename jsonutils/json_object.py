import json
import os


class JsonObject:
    def __init__(self, file: str, dict_default: dict = None, saved_destroy=True):
        if os.path.isfile(file):
            with open(file, "r") as f:
                self.dic = json.load(f)
        else:
            if dict_default is None:
                self.dic = {}
            else:
                self.dic = dict_default
        self.file = file
        self.saved_destroy = saved_destroy
    
    def __del__(self):
        if self.saved_destroy:
            self.save()

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.dic, f, indent=4)