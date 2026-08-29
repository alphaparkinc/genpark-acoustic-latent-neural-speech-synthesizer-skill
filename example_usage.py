from client import AcousticLatentNeuralSpeechSynthesizerClient

def main():
    client = AcousticLatentNeuralSpeechSynthesizerClient()
    res = client.synthesize_acoustic_tokens_to_speech('Quantum supremacy demonstration achieved using 72 superconducting qubits.')
    print('Acoustic Speech Synthesis: ' + res['acoustic_synthesis_id'])
    print('Phonemes: ' + str(res['phoneme_tokens_count']) + ' -> Acoustic Latent Codes: ' + str(res['acoustic_latent_codes_generated']))
    print('Sample Rate: ' + str(res['audio_sample_rate_hz']) + ' Hz | Vocoder Passed: ' + str(res['mel_spectrogram_vocoder_passed']))
    print('WAV Audio: ' + res['synthesized_wav_audio_url'])

if __name__ == '__main__':
    main()
