import re
import sys
# Create array of string pairs,
# each a replacement term and what to replace it with.
ARRAY_OF_REPLACEMENT_TERMS = [["\n\n\n", "\n|"],
                              ["E:", "|"],
                              ["\nS:", "|"],
                              ["\nW:", "|"],
                              ["\nR:", "|"],
                              ["\nN:0", "N/A"],
                              ["\nN:", "|"]]

def main():
    print("Starting workout_data_cleanup.py\n"
        "\n"
        "************************\n"
        "* Workout Data Cleanup *\n"
        "************************")
    
    raw_data = get_pasted_multiline_text()
    data = process_workout_data("".join(raw_data))
    print(data)

    print("Exiting Script....")

def get_pasted_multiline_text():
    # Known bug where this doesn't return if the pasted text doesn't end with a newline char
    
    print("Please paste your data below using Ctrl+Shift+V.\n"
        "When you are done, press Ctrl+D for Linux/Mac or Ctrl+Z for Windows.\n")
    try:
        lines = sys.stdin.readlines()
    except EOFError:
        pass
    return lines

def process_workout_data(raw_data):
    
    for shorthand_term, replacement in ARRAY_OF_REPLACEMENT_TERMS:
        processed_data = re.sub(shorthand_term, replacement, raw_data)

    return processed_data

def print_workout_data(data):
    print(f"\n"
        "\n"
        "Your formatted data is printed below:\n"
        "\n"
        "|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n"
        "|---|---|---|---|---|\n"
        "{data}\n"
        "\n")
    
    
if __name__ == "__main__":
    main()
