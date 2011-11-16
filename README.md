What is this?
----------------
This is a simple utility that converts a given image into base64 data that can be used as the SRC in an HTML IMG tag.

Use
----------------
You'll need to specify that your SRC tag is using embedded data like the example below:

&lt; img src="data:image/png;base64,YOUR_ENCODED_DATA_GOES_HERE"/&gt;

Note that you'll have to specify the appropriate data type for this to work.

This code in this repo is released under the MIT license. See license.txt