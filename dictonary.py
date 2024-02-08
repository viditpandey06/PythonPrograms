class Dictionary:
    def __init__(self):
        self.entries = {}

    def add_entry(self, word, definition):
        self.entries[word] = definition

    def remove_entry(self, word):
        if word in self.entries:
            del self.entries[word]

    def search_entry(self, word):
        if word in self.entries:
            return self.entries[word]
        else:
            return "Entry not found."

    def list_entries(self):
        return self.entries

# Example usage
my_dictionary = Dictionary()

my_dictionary.add_entry("apple", "A fruit that is typically red or green.")
my_dictionary.add_entry("car", "A four-wheeled motor vehicle.")

print(my_dictionary.search_entry("apple"))
print(my_dictionary.search_entry("banana"))

my_dictionary.remove_entry("car")

print(my_dictionary.list_entries())