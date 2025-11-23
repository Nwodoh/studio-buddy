const payload = {
  filename: "test.wav",
  data: "A".repeat(1398086), // ~1.6 MB of 'A' like your base64
  textPrompt: "Frontend",
};

async function testAPI() {
  try {
    const res = await fetch("http://127.0.0.1:5000/api/generate_audio/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    console.log(data);
  } catch (e) {
    console.log(e);
  }
}

testAPI();
