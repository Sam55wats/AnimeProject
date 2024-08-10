import json
import os
import glob

def character_appearances(directory):
    character_appearances = {}

    for filename in glob.glob(os.path.join(directory, '*.json')):
        with open(filename, 'r') as f:
            data = json.load(f)

            number = data['chapter_number']

            for character in data.get('characters', [])


