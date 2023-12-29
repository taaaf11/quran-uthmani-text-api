from modules import surah_aya
from flask import Flask


app = Flask(__name__)


@app.route('/<int:surah>,<int:ayah>', methods=['GET'])
def get_ayah(surah: int, ayah: int):
    ayah_data = surah_aya[f'{surah}:{ayah}']
    text = ayah_data[0]
    font = ayah_data[1]
    result = {
        'text': text,
        'font': font
    }
    return result


@app.route('/<int:surah>,<string:ayah_range>', methods=['GET'])
def get_ayahs_range(surah: int, ayah_range: str):
    ayah_texts = []
    fonts_list = []

    index = str(surah) + ',' + ayah_range
    index_split = index.split(',')
    
    for i in range(int(index_split[1].split('-')[0]), int(index_split[1].split('-')[1])+1):
        ayah_data = surah_aya[f'{index_split[0]}:{i}']
        text = ayah_data[0]
        font = ayah_data[1]
        ayah_texts.append(text)
        fonts_list.append(font)
    
    # remove duplicate values
    fonts_list = sorted(set(fonts_list))

    result = {
        'text': ''.join(ayah_texts),
        'fonts': fonts_list
    }
    return result


if __name__ == '__main__':
    app.run()
