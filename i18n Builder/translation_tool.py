import xml.etree.ElementTree as ET

import hashlib
import re
import json
import os
import shutil
import time


# Unique ID and text
extracted_text = {}
# 30,000 characters per request
ONE_REQUEST_LENGTH_RESTRICTION = 30000
# 100,000 characters per 100 seconds
LENGTH_PER_100_RESTRICTION = 100000
# Number of past characters input to API
text_count_history = 0
# Time start in API
start_time = 0
# Time spent in API
elapsed_time = 0
unique_id_history = {}


class TranslationTool:
    def __init__(self):
        self.extracted_text = {}
        self.ONE_REQUEST_LENGTH_RESTRICTION = 30000
        self.LENGTH_PER_100_RESTRICTION = 100000
        self.text_count_history = 0
        self.start_time = time.time()
        self.elapsed_time = time.time()
        self.unique_id_history = {}

    def execute(self, original_file='target_en.html', target_language="jp"):

        # Translation file creation
        target_file = original_file.replace('en', target_language)
        shutil.copyfile(original_file, target_file)

        json_file = 'unique_id_history_en.json'.replace('en', target_language)

        if os.path.isfile(json_file):
            self.unique_id_history = self.read_json(self, json_file)

        self.extract_text_from_html(self, original_file, self.extracted_text)

        self.start_time = time.time()
        for k in self.extracted_text.keys():
            if k not in self.unique_id_history:
                self.extracted_text[k] = self.conduct_restrict_api(self, self.extracted_text[k])
                self.unique_id_history.setdefault(k, self.extracted_text[k])
            else:
                self.extracted_text[k] = self.unique_id_history[k]

        tree = ET.parse(target_file)
        # XMLを取得
        root = tree.getroot()
        self.replace_text(self, root)
        tree.write(target_file, encoding='UTF-8')

        with open(json_file, 'w') as fw:
            # json.dump関数でファイルに書き込む
            json.dump(self.unique_id_history, fw, indent=2, ensure_ascii=False)

    @staticmethod
    def extract_text(self, root, storage_location_dic):
        for child in root:
            str = child.text
            if str is not None:
                str = child.text
                pattern = '^\n'

                result = re.match(pattern, str)
                if not result:
                    storage_location_dic.setdefault(hashlib.md5(str.encode()).hexdigest(), child.text)
            self.extract_text(self, child, storage_location_dic)

    @staticmethod
    def replace_text(self, root):
        for child in root:
            str = child.text
            if str is not None:
                str = child.text
                pattern = '^\n'

                result = re.match(pattern, str)
                if not result:

                    if hashlib.md5(str.encode()).hexdigest() in self.extracted_text.keys():
                        child.text = self.extracted_text[hashlib.md5(str.encode()).hexdigest()]
            self.replace_text(self, child)

    @staticmethod
    def mock_translate_api(self, str):
        translated_str = '翻訳されました_' + str + '_翻訳されました'
        return translated_str

    @staticmethod
    def conduct_restrict_api(self, text):
        translated_text = ''
        text_array = []
        # check 30,000 characters per request
        if self.is_over_one_request_restrict(self, text):
            text_array = re.findall(r"[\w']+|[.,!?;]", text)

        if len(text_array) == 0:
            translated_text = self.restrict_api(self, text)

        else:
            for text_split in text_array:
                translated_text += self.restrict_api(self, text_split)

        return translated_text

    @staticmethod
    def is_over_one_request_restrict(self, text):
        text_length = len(text)
        if text_length >= self.ONE_REQUEST_LENGTH_RESTRICTION :
            return True
        return False

    @staticmethod
    def is_over_per_100sec_restrict(self, text):
        text_length = len(text)
        self.text_count_history += text_length
        self.elapsed_time = time.time() - self.start_time
        if self.elapsed_time < 100:
            if self.text_count_history >= self.LENGTH_PER_100_RESTRICTION:
                return True
            return False
        return False

    @staticmethod
    def restrict_api(self, text):
        while self.is_over_per_100sec_restrict(self, text):
            time.sleep(1)
            self.restrict_api(self, text)

        if self.elapsed_time > 100:
            self.start = time.time()
            self.elapsed_time = time.time()
            self.text_count_history = text

        return self.mock_translate_api(self, text)

    @staticmethod
    def extract_text_from_html(self, original_file, storage_location_dic):
        # XMLファイルを解析
        tree = ET.parse(original_file)

        # XMLを取得
        root = tree.getroot()
        self.extract_text(self, root, storage_location_dic)

    @staticmethod
    def read_json(self, file):
        # 過去のjsonファイル読み込み
        with open(file) as fw:
            return json.load(fw)





