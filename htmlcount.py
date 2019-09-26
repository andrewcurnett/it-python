from banner import banner
import os

banner("HTML TAG COUNTER", "Andrew Curnett")
again = 'Y'
print("Welcome to the HTML tag counter")
while again:
    def load(filename):
        data = []
        print(f"..........loading from {filename}")
        if os.path.exists(filename):
            with open(filename) as fin:
                for entry in fin.readlines():
                    data.append(entry.rstrip())

        return data

    def html_tag_counter(text):
        text = str(text)
        tag_count = 0
        previous_char = None
        for char in text:
            if char != "/" and previous_char == "<":
                tag_count += 1
            previous_char = char
        return tag_count



    filename = input("Please enter the name of an HTML file: ")
    data = load(filename)
    print("")
    print(f"That html file has {html_tag_counter(data)} tags")

    again = input("Would you like to count another HTML file?(Y/N) ")
    print('')

    if again.upper == 'Y':
        continue

    if again.upper == 'N':
        print('\n' * 100)

