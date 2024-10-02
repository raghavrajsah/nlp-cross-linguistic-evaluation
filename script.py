import os
import csv

def process_folders_and_save_tsv(output_file, folder):
    sentid = 1
    pairid = 1
    contextid = 1
    result = []

    # Loop through each file in the folder
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # Loop through every pair of True/False sentences
            for i in range(0, len(lines), 2): 
                true_sentence = lines[i].strip()
                false_sentence = lines[i + 1].strip()

                # Split the lines by tab to get the label and sentence
                true_label, true_text = true_sentence.split('\t')
                false_label, false_text = false_sentence.split('\t')
                true_comp = 'expected' if true_label == 'True' else 'unexpected'
                false_comp = 'expected' if false_label == 'True' else 'unexpected'

                
                true_words = true_text.split()
                false_words = false_text.split()
                
                # Find the differing word (lemma) and its index (ROI)
                lemmat = ''
                lemmaf = ''
                roi_index = -1
                for j in range(min(len(true_words), len(false_words))): #in case sentences not same length it will take min
                    if true_words[j] != false_words[j]:
                        lemmat = true_words[j] # for true sentences
                        lemmaf = false_words[j] # for false sentences
                        roi_index = j
                        break
                # Create the "condition" field
                condition = f"{filename}"
                condition = condition[:-4]
                # Append data for the True sentence
                result.append({
                    'sentid': sentid,
                    'comparison': true_comp,
                    'pairid': pairid,
                    'contextid': contextid,
                    'lemma': lemmat,
                    'condition': condition,
                    'sentence': true_text,
                    'ROI': roi_index
                })
                sentid += 1

                # Append data for the False sentence
                result.append({
                    'sentid': sentid,
                    'comparison': false_comp,
                    'pairid': pairid,
                    'contextid': contextid,
                    'lemma': lemmaf,
                    'condition': condition,
                    'sentence': false_text,
                    'ROI': roi_index
                })
                sentid += 1

                # Increment pairid after each True/False pair
                pairid += 1

        # Increment contextid after processing each file
        contextid += 1

    # Save the result to a TSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
        fieldnames = ['sentid', 'comparison', 'pairid', 'contextid', 'lemma', 'condition', 'sentence', 'ROI']
        writer = csv.DictWriter(tsvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for row in result:
            writer.writerow(row)

    print(f"Data has been saved to {output_file}")

# Folders:
process_folders_and_save_tsv('output_english.tsv', 'en_evalset')
process_folders_and_save_tsv('output_dutch.tsv', 'de_evalset')
process_folders_and_save_tsv('output_french.tsv', 'fr_evalset')
process_folders_and_save_tsv('output_hebrew.tsv', 'he_evalset')
process_folders_and_save_tsv('output_russian.tsv', 'ru_evalset')

