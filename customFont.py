
"""
This module defines the byte data for the characters '0' to '9' and ':' in a 17x24 monochrome format.
It also provides functions to convert the monochrome data to RGB565 format and to create a FrameBuffer bitmap from the byte data.
"""

import framebuf


# Define the byte data for the '0' character
byte_data = [
	# @1152 '0' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x03, 0xC0, 0x00, #       ####
	0x07, 0xE0, 0x00, #      ######
	0x0C, 0x30, 0x00, #     ##    ##
	0x0C, 0x30, 0x00, #     ##    ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x0C, 0x30, 0x00, #     ##    ##
	0x0C, 0x30, 0x00, #     ##    ##
	0x07, 0xE0, 0x00, #      ######
	0x03, 0xC0, 0x00, #       ####
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '1' character
byte_data_1 = [
	# @1224 '1' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x80, 0x00, #         #
	0x07, 0x80, 0x00, #      ####
	0x1F, 0x80, 0x00, #    ######
	0x1D, 0x80, 0x00, #    ### ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x1F, 0xF8, 0x00, #    ##########
	0x1F, 0xF8, 0x00, #    ##########
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '2' character
byte_data_2 = [
	# @1296 '2' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x07, 0xC0, 0x00, #      #####
	0x1F, 0xF0, 0x00, #    #########
	0x38, 0x30, 0x00, #   ###     ##
	0x30, 0x18, 0x00, #   ##       ##
	0x30, 0x18, 0x00, #   ##       ##
	0x00, 0x18, 0x00, #            ##
	0x00, 0x30, 0x00, #           ##
	0x00, 0x60, 0x00, #          ##
	0x01, 0xC0, 0x00, #        ###
	0x03, 0x80, 0x00, #       ###
	0x06, 0x00, 0x00, #      ##
	0x0C, 0x00, 0x00, #     ##
	0x18, 0x00, 0x00, #    ##
	0x3F, 0xF8, 0x00, #   ###########
	0x3F, 0xF8, 0x00, #   ###########
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '3' character
byte_data_3 = [
	# @1368 '3' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x03, 0xC0, 0x00, #       ####
	0x0F, 0xE0, 0x00, #     #######
	0x0C, 0x70, 0x00, #     ##   ###
	0x00, 0x30, 0x00, #           ##
	0x00, 0x30, 0x00, #           ##
	0x00, 0x60, 0x00, #          ##
	0x03, 0xC0, 0x00, #       ####
	0x03, 0xE0, 0x00, #       #####
	0x00, 0x70, 0x00, #          ###
	0x00, 0x18, 0x00, #            ##
	0x00, 0x18, 0x00, #            ##
	0x00, 0x18, 0x00, #            ##
	0x18, 0x38, 0x00, #    ##     ###
	0x1F, 0xF0, 0x00, #    #########
	0x0F, 0xC0, 0x00, #     ######
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '4' character
byte_data_4 = [
	# @1440 '4' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0xE0, 0x00, #         ###
	0x01, 0xE0, 0x00, #        ####
	0x01, 0xE0, 0x00, #        ####
	0x03, 0x60, 0x00, #       ## ##
	0x06, 0x60, 0x00, #      ##  ##
	0x06, 0x60, 0x00, #      ##  ##
	0x0C, 0x60, 0x00, #     ##   ##
	0x0C, 0x60, 0x00, #     ##   ##
	0x18, 0x60, 0x00, #    ##    ##
	0x30, 0x60, 0x00, #   ##     ##
	0x3F, 0xF8, 0x00, #   ###########
	0x3F, 0xF8, 0x00, #   ###########
	0x00, 0x60, 0x00, #          ##
	0x03, 0xF8, 0x00, #       #######
	0x03, 0xF8, 0x00, #       #######
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '5' character
byte_data_5 = [
	# @1512 '5' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x1F, 0xF0, 0x00, #    #########
	0x1F, 0xF0, 0x00, #    #########
	0x18, 0x00, 0x00, #    ##
	0x18, 0x00, 0x00, #    ##
	0x18, 0x00, 0x00, #    ##
	0x1B, 0xC0, 0x00, #    ## ####
	0x1F, 0xF0, 0x00, #    #########
	0x1C, 0x30, 0x00, #    ###    ##
	0x00, 0x18, 0x00, #            ##
	0x00, 0x18, 0x00, #            ##
	0x00, 0x18, 0x00, #            ##
	0x00, 0x18, 0x00, #            ##
	0x30, 0x30, 0x00, #   ##      ##
	0x3F, 0xF0, 0x00, #   ##########
	0x0F, 0xC0, 0x00, #     ######
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '6' character
byte_data_6 = [
	# @1584 '6' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0xF8, 0x00, #         #####
	0x03, 0xF8, 0x00, #       #######
	0x07, 0x00, 0x00, #      ###
	0x0E, 0x00, 0x00, #     ###
	0x0C, 0x00, 0x00, #     ##
	0x18, 0x00, 0x00, #    ##
	0x1B, 0xC0, 0x00, #    ## ####
	0x1F, 0xF0, 0x00, #    #########
	0x1C, 0x30, 0x00, #    ###    ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x0C, 0x38, 0x00, #     ##    ###
	0x0F, 0xF0, 0x00, #     ########
	0x03, 0xE0, 0x00, #       #####
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '7' character
byte_data_7 = [
	# @1656 '7' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x1F, 0xF8, 0x00, #    ##########
	0x1F, 0xF8, 0x00, #    ##########
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x38, 0x00, #    ##     ###
	0x00, 0x30, 0x00, #           ##
	0x00, 0x30, 0x00, #           ##
	0x00, 0x70, 0x00, #          ###
	0x00, 0x60, 0x00, #          ##
	0x00, 0x60, 0x00, #          ##
	0x00, 0xE0, 0x00, #         ###
	0x00, 0xC0, 0x00, #         ##
	0x00, 0xC0, 0x00, #         ##
	0x01, 0xC0, 0x00, #        ###
	0x01, 0x80, 0x00, #        ##
	0x01, 0x80, 0x00, #        ##
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '8' character
byte_data_8 = [
	# @1728 '8' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x07, 0xE0, 0x00, #      ######
	0x0F, 0xF0, 0x00, #     ########
	0x1C, 0x38, 0x00, #    ###    ###
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x0C, 0x30, 0x00, #     ##    ##
	0x07, 0xE0, 0x00, #      ######
	0x07, 0xE0, 0x00, #      ######
	0x0C, 0x30, 0x00, #     ##    ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x1C, 0x38, 0x00, #    ###    ###
	0x0F, 0xF0, 0x00, #     ########
	0x07, 0xE0, 0x00, #      ######
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the '9' character
byte_data_9 = [
	# @1800 '9' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x07, 0xC0, 0x00, #      #####
	0x0F, 0xF0, 0x00, #     ########
	0x1C, 0x30, 0x00, #    ###    ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x18, 0x18, 0x00, #    ##      ##
	0x0C, 0x38, 0x00, #     ##    ###
	0x0F, 0xF8, 0x00, #     #########
	0x03, 0xD8, 0x00, #       #### ##
	0x00, 0x18, 0x00, #            ##
	0x00, 0x30, 0x00, #           ##
	0x00, 0x70, 0x00, #          ###
	0x00, 0xE0, 0x00, #         ###
	0x1F, 0xC0, 0x00, #    #######
	0x1F, 0x00, 0x00, #    #####
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

# Define the byte data for the ':' character
byte_data_colon = [
	# @1872 ':' (17 pixels wide)
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x03, 0xC0, 0x00, #       ####
	0x03, 0xC0, 0x00, #       ####
	0x03, 0xC0, 0x00, #       ####
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x03, 0xC0, 0x00, #       ####
	0x03, 0xC0, 0x00, #       ####
	0x03, 0xC0, 0x00, #       ####
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
	0x00, 0x00, 0x00, #
]

def monochrome_to_rgb565(byte_data, width, height, color, invert=False):
    # Create a new bytearray with the size of the image in RGB565 format
    buffer = bytearray(width * height * 2)
    fb_mono = framebuf.FrameBuffer(bytearray(byte_data), width, height, framebuf.MONO_HLSB)
    fb_rgb = framebuf.FrameBuffer(buffer, width, height, framebuf.RGB565)
    
    bg_color = TEXT_COLOR_DARK if color == TEXT_COLOR else TEXT_COLOR

    # Convert the monochrome data to RGB565 data
    for y in range(height):
        for x in range(width):
            pixel = fb_mono.pixel(x, y)
            # fb_rgb.pixel(x, y, color if pixel else 0)
            if not invert:
                fb_rgb.pixel(x, y, color if pixel else bg_color)
            else:
                fb_rgb.pixel(x, y, color if not pixel else 0)


    return fb_rgb

# Convert the byte data to a FrameBuffer bitmap
def bitmap_to_framebuffer(byte_data, width, height):
    # Create a bytearray with the size of the image
    buffer = bytearray(byte_data)
    # Create a FrameBuffer with MONO_HLSB format
    return framebuf.FrameBuffer(buffer, width, height, framebuf.MONO_HLSB)

# Define the color for the text
TEXT_COLOR = 0xFFFF  # White in RGB565 format
TEXT_COLOR_DARK = 0x0000  # Black in RGB565 format


# Define the bitmaps as FrameBuffer objects
bitmaps = {
    '0': monochrome_to_rgb565(byte_data, 17, 24, TEXT_COLOR),  # Width and height of the character '0'
    '1': monochrome_to_rgb565(byte_data_1, 17, 24, TEXT_COLOR),  # Width and height of the character '1'
    '2': monochrome_to_rgb565(byte_data_2, 17, 24, TEXT_COLOR),  # Width and height of the character '2'
    '3': monochrome_to_rgb565(byte_data_3, 17, 24, TEXT_COLOR),  # Width and height of the character '3'
    '4': monochrome_to_rgb565(byte_data_4, 17, 24, TEXT_COLOR),  # Width and height of the character '4'
    '5': monochrome_to_rgb565(byte_data_5, 17, 24, TEXT_COLOR),  # Width and height of the character '5'
    '6': monochrome_to_rgb565(byte_data_6, 17, 24, TEXT_COLOR),  # Width and height of the character '6'
    '7': monochrome_to_rgb565(byte_data_7, 17, 24, TEXT_COLOR),  # Width and height of the character '7'
    '8': monochrome_to_rgb565(byte_data_8, 17, 24, TEXT_COLOR),  # Width and height of the character '8'
    '9': monochrome_to_rgb565(byte_data_9, 17, 24, TEXT_COLOR),  # Width and height of the character '9'
    ':': monochrome_to_rgb565(byte_data_colon, 17, 24, TEXT_COLOR),  # Width and height of the character ':'
}

# Dark Bitmaps
bitmaps_dark = {
	'0': monochrome_to_rgb565(byte_data, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '0'
    '1': monochrome_to_rgb565(byte_data_1, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '1'
    '2': monochrome_to_rgb565(byte_data_2, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '2'
    '3': monochrome_to_rgb565(byte_data_3, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '3'
    '4': monochrome_to_rgb565(byte_data_4, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '4'
    '5': monochrome_to_rgb565(byte_data_5, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '5'
    '6': monochrome_to_rgb565(byte_data_6, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '6'
    '7': monochrome_to_rgb565(byte_data_7, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '7'
    '8': monochrome_to_rgb565(byte_data_8, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '8'
    '9': monochrome_to_rgb565(byte_data_9, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character '9'
    ':': monochrome_to_rgb565(byte_data_colon, 17, 24, TEXT_COLOR_DARK),  # Width and height of the character ':'
}  
