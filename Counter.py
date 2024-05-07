print("Counter.py is starting...")
from collections import Counter
def count_word_frequencies(text):
  words = [word.lower().strip() for word in text.split()]
  word_counts = Counter(words)
  return word_counts
def sort_word_frequencies(word_counts):
  sorted_frequencies = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
  return sorted_frequencies
def write_word_frequencies_to_file(sorted_frequencies, filename):
  with open(filename, 'w') as file:
    for word, count in sorted_frequencies:
      file.write(f"{word} : {count}\n")
def main():
  input_filename = input("Enter the name of the text file: ")
  try:
    with open(input_filename, 'r') as file:
      text = file.read()
  except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found.")
    return
  word_counts = count_word_frequencies(text)
  sorted_frequencies = sort_word_frequencies(word_counts)
  output_filename = input("Enter the name of the output file (will be overwritten): ")
  write_word_frequencies_to_file(sorted_frequencies, output_filename)
  print(f"Word frequencies written to '{output_filename}'.")
print("Imports loaded and functions defined...")
main()