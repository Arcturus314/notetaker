This is a small project aimed to enhance the typical note-taking and study routine. Aimed to parse text files, parser.py will create notecards for definitions embedded in a notes file, indicated through the use of keywords.

The general formatting of a definition can be seen below:

[...]
... def| item name:item definition
[...]

For each instance of 'def| item name:item definition', the script will create a line in an output file that can be imported as a notecard by the revision tool Anki.

To run the parser, use the command: python parser.py <inputfile> <outputfile>
