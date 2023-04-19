import yaml
import os


class ParseYaml:
    def __init__(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        self.yaml_path = os.path.join(cur_path, "../test/library/data.yaml")

    def load_data(self):
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            try:
                data = yaml.load(f, Loader=yaml.FullLoader)
                print(data)
                return data
            except yaml.YAMLError as e:
                print(e)

#
# pa = ParseYaml()
# pa.load_data()
