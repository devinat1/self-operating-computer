import os
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    agent_prompts_directory = '../../prompt-creator/prompts-text'

    for filename in os.listdir(agent_prompts_directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(agent_prompts_directory, filename)
            with open(filepath, 'r') as file:
                lines = file.readlines()
                site = lines[0]
                print(site)
                for line in lines[1:]:
                    # command = f'operate --prompt "go to {site} and do the following: {line}"'.replace('\n', '')
                    # command = f'operate -m gpt-4-with-ocr --prompt "go to {site} and do the following: {line}"'.replace('\n', '')
                    command = f'operate -m gpt-4-with-som --prompt "go to {site} and do the following: {line}. Always start by opening google chrome."'.replace('\n', '')
                    # command = f'operate -m llava --prompt "go to {site} and do the following: {line}"'.replace('\n', '')
                    # command = f'operate -m gpt-4 --prompt "go to {site} and do the following: {line}, Always start by opening google chrome."'.replace('\n', '')
                    print(command)
                    os.system(command)