from flask import Flask, jsonify
from data import surah_aya


app = Flask(__name__)


@app.route('/<int:surah>,<int:ayah>', methods=['GET'])
def get_ayah(surah, ayah):
    ayah_data = surah_aya[f'{surah}:{ayah}']
    text = ayah_data[0]
    font = ayah_data[1]
    result = jsonify({'text': text,
              'font': font})
    return result


if __name__ == '__main__':
    app.run(debug=True)
