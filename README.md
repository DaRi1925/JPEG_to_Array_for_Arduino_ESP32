# JPEG to Array Converter for Arduino/ESP32
## Project Description
This project is a Python application for converting JPEG and PNG images into a data array that can be used in Arduino and ESP32 sketches. The program is specifically designed to work with the ST7789V 2.0-inch TFT display (240x320, SPI interface).

### How the Program Works
The application provides a graphical interface using the Tkinter library, where users can select an image for conversion. Once an image is chosen, it’s processed and converted into an RGB565 data array compatible with the ST7789V TFT display, then saved in the image_array.txt file.

-  RGB to RGB565 Conversion: Each pixel is converted from RGB format to RGB565, a color format optimized for TFT displays. This reduces memory usage and improves display performance.
-  Supported Formats: Users can select both JPEG and PNG files.
-  Array Generation: The converted image data is saved in image_array.txt. Values are formatted as 0xFFFF, separated by commas, and aligned in rows of 16 values for easy readability.
### Requirements
- Python 3.x
- Libraries:
Pillow (for image processing)
tkinter (for the graphical interface)
To install the Pillow dependency, use the following command:

```bash
pip install pillow
```

## Display Example
![Display](img211249.png)


## Usage Instructions

1. Run the program by right-clicking on the convert.py.exe.py file, selecting "Open with", and choosing Python.

2. In the graphical interface that appears, click the "Select Image" button and choose a JPEG or PNG file.

3. The program will convert the image and save the data array in image_array.txt.

4. Open image_array.txt, copy the array, and paste it into your Arduino/ESP32 sketch to display the image on your TFT screen.
 

## Installation and Running

To start the application, simply right-click on 'convert.py.exe.py' and choose "Open with Python".

## License
This project is licensed under the MIT License.
