import pyfiglet

def generate_ascii_art(input_text):
    # write ascii emoji by using pyfiglet
    ascii_art = pyfiglet.figlet_format(input_text)
    return ascii_art

def main():
    print("ASCII Emoji Generator")
    print("=====================")
    text = input("Enter your message : ")
    art = generate_ascii_art(text)
    print("\n This is your ASCII emoji :\n")
    print(art)

if __name__ == "__main__":
    main()