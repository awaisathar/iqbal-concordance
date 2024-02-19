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

# Adjust the file path for compatibility and flexibility
text_files_path = os.path.join('public', 'text', '*.txt')
files = natsorted(glob.glob(text_files_path))

if not files:
    print(f"No text files found in {text_files_path}. Please check the directory path.")
else:
    print(f"Processing {len(files)} text files...")

    for file_path in files:
        try:
            with open(file_path, 'r', encoding='utf-8') as infile:
                lines = infile.readlines()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue  # Skip to the next file if an error occurs
        
        line_count = 0
        first = True
        last_line_was_special = False
        is_special_line = False

        for line_count in range(0, len(lines)):
            line = lines[line_count].strip()

            # handle ghazals with two empty lines in the start
            if line_count == 1 and len(line) == 0:
                line = '٭'

            if len(line) == 0:
                continue

            last_line_was_special = is_special_line
            is_special_line = (line_count == 1
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
                if word != '':
                    end = start + len(word)
                    entry = {
                        'line': line,
                        'start': start,
                        'end': end,
                        'line_number': line_count+1,
                        'file': int(re.search(r'\d+', os.path.basename(file_path)).group()),
                        'first': first
                    }

                    if not is_special_line:
                        entry['other'] = lines[line_count+1].strip() if first else lines[line_count-1].strip()

                    norm = normalise(word)

                    if word != '':
                        if not norm in all_tokens:
                            all_tokens[norm] = []
                        all_tokens[norm].append(entry)
                    try:
                        delimiter = next(filter(None, re.split(f'({regex_pattern})', line[end:])))
                        start = end + len(delimiter)
                    except StopIteration:
                        break
                    # Move to the next line if no more tokens are found
            # end word in tokens
        # end lines in file
    # end with current file
# end files in folder

    print(f"Finished processing all files. Total unique tokens: {len(all_tokens)}")
try:
    collator = Collator.createInstance(Locale("ur_PK"))
    all_tokens_sorted = dict(sorted(all_tokens.items(), key=lambda item: collator.getSortKey(item[0])))

    # Calculate word frequencies
    word_frequencies = {word: len(details) for word, details in all_tokens_sorted.items()}

    # Write concordance.json with compiled occurrences
    with open('concordance.json', 'w', encoding='utf-8') as out:
        json.dump(all_tokens_sorted, out, indent=2, ensure_ascii=False)
    print("Successfully wrote concordance.json")

    # Prepare words with frequencies for words.json
    words_with_frequencies = {word: {'frequency': freq} for word, freq in word_frequencies.items()}

    # Write words with frequencies to words.json
    with open('src/assets/words.json', 'w', encoding='utf-8') as out:
        json.dump(words_with_frequencies, out, indent=2, ensure_ascii=False)
    print("Successfully witten words into src/assets/words.json.")

except Exception as e:
    print(f"Error during processing: {e}")

# Directory and individual word files creation logic
try:
    shutil.rmtree('public/words')
except FileNotFoundError:
    pass  # No action needed if directory does not exist
except Exception as e:
    print(f"Error removing 'public/words' directory: {e}")

for word in set(w[0] for w in all_tokens):
    os.makedirs(os.path.join('public', 'words', word), exist_ok=True)

for word, entries in all_tokens_sorted.items():
    try:
        with open(os.path.join('public', 'words', word[0], f"{word}.json"), 'w', encoding='utf-8') as out:
            json.dump(entries, out, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error writing file for word '{word}': {e}")