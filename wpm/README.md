# WORDS PER MINUTE

### Description
This program is designed to calculate the user's typing speed as words per minute. When executed, the program initially prints the following message to the stdout stream:

Please type: The quick brown fox jumps over the lazy dog
Press enter when ready and again when finished.

The user is prompted to press the enter key, type the given phrase, and then press the enter key for a second time. The program measures the time between the first press of the enter key and the second press of the enter key to the nearest hundredth of a second. Given that the phrase is typed correctly, the program then calculates the user's typing speed by performing the following operations: ( number of words in phrase: 9 ) / ( total time ). The typing speed is then displayed.

### Error Checking
If the user fails to correctly type the given phrase, an error message will appear indicating that the user must try again in order for an accurate calculation to be made.