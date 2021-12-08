import torch
from torch import cuda
import json
import nltk

from transformers import BertTokenizerFast
from nltk import word_tokenize

nltk.download('punkt')


def load_model(device):
    path = './model/aviation-accidents.pt'
    loaded_model = torch.load(path, map_location=torch.device(device))
    loaded_model.to(device)

    return loaded_model


def load_tokenizer():
    # Save tokenizer?
    BERT_MODEL_NAME = 'bert-base-uncased'
    tokenizer = BertTokenizerFast.from_pretrained(BERT_MODEL_NAME)

    return tokenizer


def load_data():
    # Load data
    f = open('./model/data.json', )
    data = json.load(f)
    data['index2tag'] = {int(k): v for k, v in data['index2tag'].items()}

    f.close()
    return data


def modelInit():
    # CARGAMOS EL MODELO
    print("--> Loading the model. Please wait.\n")

    device = 'cuda' if cuda.is_available() else 'cpu'
    loaded_model = load_model(device)
    tokenizer = load_tokenizer()
    data = load_data()

    return device, loaded_model, tokenizer, data


def inference(modelData, sentence):
    device, loaded_model, tokenizer, data = modelData

    inputs = tokenizer(word_tokenize(sentence),
                       is_split_into_words=True,
                       return_offsets_mapping=True,
                       padding='max_length',
                       truncation=True,
                       max_length=data['max_seq_len'],
                       return_tensors="pt")
    # move to gpu
    ids = inputs["input_ids"].to(device)
    mask = inputs["attention_mask"].to(device)

    outputs = loaded_model(ids, attention_mask=mask)
    logits = outputs[0]

    active_logits = logits.view(-1, loaded_model.num_labels)  # shape (batch_size * seq_len, num_labels)
    flattened_predictions = torch.argmax(active_logits,
                                         axis=1)  # shape (batch_size*seq_len,) - predictions at the token level

    tokens = tokenizer.convert_ids_to_tokens(ids.squeeze().tolist())
    token_predictions = [data['index2tag'][i] for i in flattened_predictions.cpu().numpy()]
    wp_preds = list(zip(tokens, token_predictions))  # list of tuples.  Each tuple = (wordpiece, prediction)

    prediction = []
    for token_pred, mapping in zip(wp_preds, inputs["offset_mapping"].squeeze().tolist()):
        # only predictions on first word pieces are important
        if mapping[0] == 0 and mapping[1] != 0:
            prediction.append(token_pred[1])
        else:
            continue


    output = []

    '''for word, tag in zip(word_tokenize(sentence), prediction):
        output.append({word: tag})

    return json.dumps(output)'''

    tag_temp = ''
    accumulate_word = ''
    bio = False
    characters = [',',  '.', ';', '/', '?', '!', '-', ':', '_', '—', '–']

    for word, tag in zip(word_tokenize(sentence), prediction):
        # Caso Outside
        if tag[0] == 'O' and bio:
            if word in characters:
                accumulate_word += word

            output.append({accumulate_word: tag_temp})
            tag_temp = ''
            accumulate_word = ''
            bio = False

        # Caso de dos tag currente != tag anterior.
        elif tag[2:] != tag_temp and bio:
            output.append({accumulate_word: tag_temp})
            # Caso de tag currente es tipo Beganning.
            if tag[0] == 'B':
                tag_temp = tag[2:]
                accumulate_word = word
                bio = True
            else:
                bio = False

        # Caso generico de inside
        elif tag[0] == 'I' and bio:
            accumulate_word = "{} {}".format(accumulate_word, word)
    
        # Caso generico de Beginning
        elif tag[0] == 'B':
            # Caso: B detras de otro B
            if bio:
                output.append({accumulate_word: tag_temp})

            tag_temp = tag[2:]
            accumulate_word = word
            bio = True
        else:
            output.append({word: ""})

    return json.dumps(output)
