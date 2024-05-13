from gtts import gTTS
from playsound import playsound

# Função que cria e salva o áudio
def create_and_save_audio(text, language, filename, slow=False):
    gtts_object = gTTS(text=text, lang=language, slow=slow)
    filepath = f"content\{filename}.wav"
    gtts_object.save(filepath)
    return filepath

# Textos para gravar
english_text_to_say = "How are you doing?"
english_language = "en"
english_filename = "gtts_english"

french_text_to_say = "Je vais au supermarché"
french_language = "fr"
french_filename = "gtts_french"

# Criar e salvar áudios
english_filepath = create_and_save_audio(english_text_to_say, english_language, english_filename)
french_filepath = create_and_save_audio(french_text_to_say, french_language, french_filename, slow=True)

# Reproduzir áudios
playsound(english_filepath)
playsound(french_filepath)