from banner import banner
import journal
banner("DEEP THOUGHTS", "Andrew Curnett")

def main():
    run_event_loop()

def run_event_loop():
    filename = input("What file would you like to load? ")
    journal_data = journal.load(filename)

    while True:
        command = input("[L]ist entries, [A]dd an entry, [D]elete an entry, E[x]it: ")

        if command.upper() == "L":
            list_entries(journal_data)
        elif command.upper() == "A":
            add_entry(journal_data)
        elif command.upper() == "D":
            delete_entry(journal_data)
        elif command.upper() == "X":
            break
        else:
            print("Sorry, I don't understand")
    journal.save(filename, journal_data)

def list_entries(data):
    print("Your journal entries:")
    entries = reversed(data)
    for num, entry in enumerate(entries):
        print(f"{num+1} - {entry}")





def add_entry(data):
    entry = input("Type your entry, <ENTER> to exit: \n")
    journal.add_entry(entry, data)
    #data.append(entry)

def delete_entry(data):
    for num, entry in enumerate(data):
        print(f"{num+1} - {entry}")
    print("")
    entry_to_delete = int(input("Which entry would you like delete? "))
    del data[entry_to_delete-1]











main()