from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
import replicate

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
        prompt = data.get('textPrompt')
        input_audio = data.get('inputAudio')
        duration = 10
        # if len(input_audio):
            # compressed = base64.b64decode(input_audio, validate=True)
            # decompressed = dctx.decompress(input_audio)

        input = {
            "prompt": prompt,
            "model_version": "stereo-large",
            "output_format": "wav",
            "normalization_strategy": "peak",
            "input_audio": input_audio,
            "duration": duration
        }

        # output = replicate.run(
        #         "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
        #         input=input
        # )

        # result_url = output.url()
        # print(result_url)

        # return jsonify({"status": "success", "textPrompt": prompt, 'audioUrl': result_url})
        return jsonify({"status": "success", "textPrompt": prompt, 'audioUrl': 'https://yedu-music.onrender.com/songs/example.wav'})
    except Exception as e:
        print(e)
        return jsonify({"status": "error"}), 403

if __name__ == "__main__":
    app.run(debug=True)

# import sounddevice as sd
# import torch
# from audiocraft.models import MusicGen
# from audiocraft.data.audio import audio_read
# from scipy.io.wavfile import write
# import numpy as np
# import uuid
# import os

# fs = 16000      
# duration = 10   
# prompt = "guitar riff"

# recording_id = str(uuid.uuid4())[:8]
# output_id = str(uuid.uuid4())[:8]
# recording_file = f"recording_{recording_id}.wav"
# output_file = f"musicgen_output_{output_id}.wav"

# print("🎙️ Recording...")
# recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
# sd.wait()
# print("✅ Recording complete!")

# write(recording_file, fs, (recording * 32767).astype(np.int16))
# print(f"💾 Recording saved as {recording_file}")

# print("🔄 Loading MusicGen Melody model...")
# model = MusicGen.get_pretrained('facebook/musicgen-melody', device='cpu')
# model.set_generation_params(duration=10)

# melody_waveform, melody_sr = audio_read(recording_file)
# if melody_sr != model.sample_rate:
#     print(f"⚠️ Resampling from {melody_sr} to {model.sample_rate}")
# melody_waveform = melody_waveform.to(model.device)

# print("🎵 Generating music from your melody and prompt...")
# wav_tensor = model.generate_with_chroma([prompt], melody_waveform[None, ...], melody_sample_rate=melody_sr)

# wav_np = wav_tensor.detach().cpu().numpy()[0, 0, :]
# wav_np = wav_np / np.max(np.abs(wav_np))
# wav_int16 = (wav_np * 32767).astype(np.int16)
# write(output_file, model.sample_rate, wav_int16)

# print(f"✅ Generated music saved as {output_file}")


# curl --silent --show-error https://api.replicate.com/v1/predictions \
# 	--request POST \
# 	--header "Authorization: Bearer $REPLICATE_API_TOKEN" \
# 	--header "Content-Type: application/json" \
# 	--header "Prefer: wait" \
# 	--data @- <<-EOM
# {
# 	"version": "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
# 	"input": {
#       "prompt": "Edo25 major g melodies that sound triumphant and cinematic. Leading up to a crescendo that resolves in a 9th harmonic",
#       "model_version": "stereo-large",
#       "output_format": "mp3",
#       "normalization_strategy": "peak"
# 	}
# }
# EOM

# // const var REPLICATE_API_TOKEN = "r8_SmSVzZBIIWIYGeVZQnFcgsknG9HHplo2yeDl3";
# // Server.setBaseURL("https://api.replicate.com");
# // Server.setHttpHeader("Content-Type: application/json");
# // Server.setHttpHeader("Content-Type: application/json");
# // Server.setHttpHeader("Prefer: wait");
# // Server.setHttpHeader("Authorization: Bearer " + REPLICATE_API_TOKEN);


# Cool summer beat: https://yedu-music.onrender.com/songs/sunflower-street-drumloop-85bpm-163900.wav
# ringtone: https://yedu-music.onrender.com/songs/example.wav
# burnaboy: https://yedu-music.onrender.com/songs/Burna-Boy-Ft-Khalid-Wild-dreams (mp3cut.net).wav

# inline function addAudioInput(component, value)
# {
# 	if (!value) {
# 	return;
# 	}
	
# 	FileSystem.browse(false, false, "*.wav;*.mp3", function(f)
# 		{
# 			if (!f || !f.isFile()) {
# 			        Console.print("No file selected");
# 			        return;
# 			}
			
# 			// base64AudioData = f.loadAsBase64String();
# 			base64AudioData = f.loadAsString();
# 			Console.print('This is the base64Data');
# 			Console.print(base64AudioData);
# 		    // result.show();
# 		});
# }

