import os
import glob
import json
import re
import unicodedata
import shutil
from natsort import natsorted
from icu import Collator, Locale 


def normalise(input_text): # remove all diacritics
    return re.sub(r'ۂ$', 'ہ', # hamza-e-izafat is a special case
                  ''.join(char for char in unicodedata.normalize('NFC', input_text) if unicodedata.category(char) != 'Mn'))


all_tokens = {}
regex_pattern = r'[\s،!,\(\)*٭"\'۔:’‘“”؟]+'

for file_path in natsorted(glob.glob('/mnt/c/awais/iqbal-concordance/public/text/*.txt')):
    with open(file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()
        line_count = 0
        first = True
        last_line_was_special = False
        is_special_line = False

        for line_count in range(0, len(lines)):

            line = lines[line_count].strip()

            # handle ghazals with two empty lines in the start
            if line_count == 0 and len(line) == 0:
                line = '٭'

            if len(line) == 0:
                continue

            last_line_was_special = is_special_line
            is_special_line = (line_count == 0
                               or line.startswith('(')
                               or line.endswith(':')
                               or len(line) == 1
                               or line.endswith('۔')
                               or line.endswith('لولاب!')
                               )

            first = (not first) or last_line_was_special
            tokens = re.split(regex_pattern, line)
            start = 0

            for word in tokens:
                end = start + len(word)
                before = line[:start].strip()
                after = line[end:].strip()
                entry = {
                    'line': line,
                    'start': start,
                    'end': end,
                    'line_number': line_count+1,
                    'file': int(re.search(r'\d+', file_path[::-1]).group()[::-1]),
                    'first': first
                }

                if not is_special_line:
                    entry['other'] = lines[line_count +
                                           1].strip() if first else lines[line_count-1].strip()

                norm = normalise(word)

                if word != '':
                    if not norm in all_tokens:
                        all_tokens[norm] = []
                    all_tokens[norm].append(entry)
                try:
                    delimiter = next(filter(None, re.split(
                        f'({regex_pattern})', line[end:])))
                    start = end + len(delimiter)
                except StopIteration:
                    break
            # end word in tokens
        # end lines in file
    # end with current file
# end files in folder

# must install Urdu locale befor this
collator = Collator.createInstance(Locale("ur_PK"))
all_tokens = dict(
    sorted(all_tokens.items(), key=lambda item: collator.getSortKey(item[0])))

with open('concordance.json', 'w', encoding='utf-8') as out: # File not used
    json.dump(all_tokens, out, indent=2, ensure_ascii=False)

try:
    shutil.rmtree('public/words')
except FileNotFoundError:
    pass

for word in set([w[0] for w in all_tokens.keys()]):
    os.makedirs(f'public/words/{word[0]}')

for word in all_tokens.keys():
    with open(f'public/words/{word[0]}/{word}.json', 'w', encoding='utf-8') as out:
        json.dump(all_tokens[word], out, indent=2, ensure_ascii=False)

with open('src/assets/words.json', 'w', encoding='utf-8') as out:
    json.dump(sorted(list(all_tokens.keys()), key=collator.getSortKey),
              out, indent=2, ensure_ascii=False)
