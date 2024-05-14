from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask_socketio import emit

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ar")


def translate_segment(segment):
    encoded_segment = tokenizer.encode(segment, return_tensors="pt", truncation=True, padding="max_length", max_length=tokenizer.model_max_length)
    translated_tokens = model.generate(encoded_segment)
    arabic_translation = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return arabic_translation


def translate_complete(english_text):

    tokens = tokenizer.tokenize(english_text)
    max_tokens = 300
    segments = []

    for i in range(0, len(tokens), max_tokens):
        segment_text = tokenizer.convert_tokens_to_string(tokens[i:i+max_tokens])
        segments.append(segment_text)

    segment_count = len(segments)
    translated_segments = []

    for index, segment in enumerate(segments):
        emit('progress', {'progress': (index / segment_count) * 100})
        translated_segments.append(translate_segment(segment))

    complete_translation = ' '.join(translated_segments)
    emit('progress', {'progress': 100})
    return complete_translation
