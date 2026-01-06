from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
import replicate
import os

load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 102

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/generate_audio/", methods=["GET", "POST"])
def generate():
    prompt = ''
    try:
        data = request.get_json()
        prompt = data.get("textPrompt")
        input_audio = data.get("inputAudio")
        duration = 10

        payload = {
            "prompt": prompt,
            "model_version": "stereo-large",
            "output_format": "wav",
            "normalization_strategy": "peak",
            # "input_audio": input_audio,
            "duration": duration,
        }

        output = replicate.run(
            "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
            input=payload,
        )

        # Inspect shape
        print("output type:", type(output))
        print("output repr:", repr(output))

        # Handle common cases safely:
        if isinstance(output, str):
            result_url = output
        elif isinstance(output, list) and output:
            first = output[0]
            if isinstance(first, dict) and "url" in first:
                result_url = first["url"]
            else:
                result_url = str(first)
        elif isinstance(output, dict) and "url" in output:
            result_url = output["url"]
        elif hasattr(output, "url"):
            # url might be attribute (string) or method
            attr = getattr(output, "url")
            result_url = attr() if callable(attr) else attr
        else:
            result_url = str(output)

        print("result_url:", result_url)

        return jsonify({"status": "success", "textPrompt": prompt, 'audioUrl': result_url})
        # return jsonify({"status": "success", "textPrompt": prompt, 'audioUrl': 'https://yedu-music.onrender.com/songs/example.wav'})
    except Exception as e:
        print(e)
        return jsonify({"status": "error"}), 403

if __name__ == "__main__":
    app.run(debug=True)