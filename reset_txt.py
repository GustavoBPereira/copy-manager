def reset_txt():
    with open('copy_manager.txt', 'w') as file:
        file.write('### Comand C mananger\n\n## Current copy\n\n## END CURRENT\n\n\n')

if __name__ == "__main__":
    reset_txt()