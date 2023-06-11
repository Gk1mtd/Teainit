def image_to_bytecode():
    with open("/home/michael/Repository/Teainit/tea.png", 'rb') as file:
        bytecode = file.read()
    print("")
    print(bytecode)
    print("")

def main():
    image_to_bytecode()
    Gtk.main()

if __name__ == '__main__':
    main()
