import json


class JSONDB:

    def __init__(self, file_path):
        self.file_path = file_path
        self.load_json()

    # r for reading
    # w for writing
    # r+ opens for reading and writing (cannot truncate a file)
    # w+ for writing and reading (can truncate a file)
    # rb+ reading or writing a binary file
    # wb+ writing a binary file
    # a+ opens for appending

    def load_json(self):
        f = open(self.file_path, 'rb+')
        txt = f.read()
        if txt == '':
            txt = '{}'
            f.seek(0)
            f.write(txt)
        f.close()
        try:
            self.json_obj = json.loads(txt)
        except:
            self.json_obj = {}

    def save_json(self):
        f = open(self.file_path, 'w')
        json_str = json.dumps(self.json_obj)
        f.write(json_str)
        f.close()

    def reload(self):
        self.load_json()
        return self

    def obj(self):
        return self.json_obj

    def get(self, key):
        if key in self.json_obj:
            return self.json_obj[key]
        else:
            return None

    def set(self, key, val, save=True):
        self.json_obj[key] = val
        if save:
            self.save_json()

    def add(self, key, key1, val):
        if key in self.json_obj:
            self.json_obj[key][key1] = val
        else:
            self.json_obj[key] = {
                key1: val
            }

        self.save_json()

    def get_bool(self, key):
        b = self.get(key)
        if not b:
            return None

        try:
            b = bool(b)
            return b
        except:
            return None

    def to_string(self):
        return json.dumps(self.json_obj)