# kpuz
Convert ipuz Crosswords to puz format.

This relies on the [puzpy](https://github.com/svisser/ipuz) and [ipuz](https://github.com/alexdej/puzpy) libraries. To install dependencies: `pip install -r requirements.txt`.

`xfer.py` takes two parameters: an ipuz input file and a puz output file.
`dump.py` dumps a puz-formatted file for easy viewing.

Inside xfer.py is a boolean flag called `output` that defaults to `True`, which means print in the puz binary format. If you want to print in the puz text format, change `output` to `False` and store it in a text file. AcrossLite will be able to read the ASCII file and convert it to binary, if you wish.

Other links:
* [Documentation on the ipuz format](http://www.ipuz.org/)
* [Documentation on the text puz format](http://www.litsoft.com/across/docs/AcrossTextFormat.pdf)
There is no meaningful documentation on the puz binary file format.

Finally, this only supports very basic format. It doesn't supportipuz-type rebus and special objects in shapes.

I'd be willing to consider tests before adding more powerful features.
