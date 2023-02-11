from vosk import Model, KaldiRecognizer
import json
import shutil

import pathlib
file_path = str( pathlib.Path(__file__).absolute().parent )

# if not os.path.exists("ModelPath"):
#     print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
#     exit (1)

class AudioProc():
    def __init__(self,entry_file=None, model_path=file_path+ r"\model"):
        self.model = Model(model_path=model_path)
        self.entry_file = entry_file

    def run(self, dest_file_name=None):
        # save uploaded file
        with open(self.entry_file.filename, 'wb') as f:
            dest_dir = file_path + r'\src\db\received_files\12\\' + self.entry_file.filename
            shutil.copyfileobj(self.entry_file.file, f)
        

        # Large vocabulary free form recognition
        rec = KaldiRecognizer(self.model, 16000)

        # You can also specify the possible word list
        #rec = KaldiRecognizer(model, 16000, "zero oh one two three four five six seven eight nine")

        # wf = open(sys.argv[0], "rb")
        if self.entry_file:
            wf = open(self.entry_file.filename, "rb")
        else:
            wf = open(file_path + f'\{dest_file_name}.mp3', "rb")
        wf.read(44) # skip header

        text_from_sound = ''
        while True:
            data = wf.read(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                res = json.loads(rec.Result())
                text_from_sound = text_from_sound + res['text'] + ' '

        
        print('extracted text:',text_from_sound)
        return text_from_sound

# result_text = AudioProc().recognizer('speech1')
# print('done')