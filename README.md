# Password Generator

A simple Python script that generates secure passwords based on user specifications for the number of letters, numbers, and symbols.

## Description

This Password Generator creates randomized passwords by combining letters (both uppercase and lowercase), numbers, and special symbols. The user can specify the exact number of each type of character they want in their password, making it highly customizable while maintaining security through randomization.

## Features

- Customizable password length
- Mix of uppercase and lowercase letters
- Inclusion of numbers (0-9)
- Special symbols (!#$%&()*+)
- Random character placement for enhanced security

## Requirements

- Python 3.x
- No additional packages required (uses only built-in `random` module)

## Installation

1. Clone this repository or download the Python file
2. No additional installation steps required

## Usage

1. Run the script:
```bash
python password_generator.py
```

2. Follow the prompts to specify:
   - Number of letters desired
   - Number of symbols desired
   - Number of numbers desired

3. The program will generate and display your password

Example interaction:
```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
8
How many symbols would you like?
2
How many numbers would you like?
2
Your password is: Kj#9nM$p2q
```

## How It Works

1. The script maintains separate lists of:
   - Letters (a-z, A-Z)
   - Numbers (0-9)
   - Symbols (!#$%&()*+)

2. Using the random module, it:
   - Randomly selects which type of character to add next
   - Randomly chooses a character from the appropriate list
   - Continues until all requested characters are included

3. The final password is constructed by joining all selected characters into a single string

## Security Features

- Characters are added in random order, not in blocks
- Uses both uppercase and lowercase letters
- Includes special symbols for added complexity
- Random selection process makes passwords unpredictable

## Limitations

- Cannot specify minimum or maximum length
- Fixed set of special symbols
- No password strength checker
- No copy to clipboard functionality

## Contributing

Feel free to fork this repository and submit pull requests to suggest improvements. Some possible enhancements could include:
- Adding password strength validation
- Expanding the symbol set
- Adding a GUI interface
- Implementing copy to clipboard functionality

## License

This project is open source and available under the MIT License.
