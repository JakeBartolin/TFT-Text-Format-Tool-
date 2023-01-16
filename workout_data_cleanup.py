import re
import sys

# Array of replacement terms + replacement values.
ARRAY_OF_REPLACEMENT_TERMS = [["\nE:", "|"],
                              ["E:",   "|"],
                              ["\nS:", "|"],
                              ["\nW:", "|"],
                              ["\nR:", "|"],
                              ["\nN:", "|"]]

def main():
    print("Starting workout_data_cleanup.py\n"
        "\n"
        "************************\n"
        "* Workout Data Cleanup *\n"
        "************************")
    
    raw_data = get_pasted_multiline_text()
    data = process_workout_data("".join(raw_data))
    print_workout_data(data)

    print("Exiting Script....")

def get_pasted_multiline_text():
    # Known bug where this doesn't return if the pasted text doesn't end
    # with a newline character.
    
    print("Please paste your data below using Ctrl+Shift+V.\n"
        "When you are done, press Ctrl+D for Linux/Mac or Ctrl+Z for Windows.\n")
    try:
        lines = sys.stdin.readlines()
    except EOFError:
        pass
    return lines

def process_workout_data(raw_data):
    # This whole thing could be alot cleaner if I used regular expressions
    # but IDK how to do those right now and it's getting late. This will
    # still not put a "|" at the end of each line, so that will need fixed.
    # 2023-01-15 JB
    for replace_key in ARRAY_OF_REPLACEMENT_TERMS:
        raw_data = re.sub(replace_key[0], replace_key[1], raw_data)

    return raw_data

def print_workout_data(data):
    print(f"\n\n"
          "****************************************\n"
          "* Your formatted data is printed below *\n"
          "****************************************\n"
          "\n"
          "|Excercise|Sets/Reps|Weight|Reserve Reps|Notes|\n"
          "|---|---|---|---|---|\n"
          f"{data}\n\n")
    
if __name__ == "__main__":
    main()
