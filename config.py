#Config settings to change behavior of photo booth
file_path = '/home/pi/Pictures/Photobooth/' # path to save images
clear_on_startup = False # True will clear previously stored photos as the program launches. False will leave all previous photos.
post_online = False # True to upload images. False to store locally only.
print_photos = True # Obvious
printer_name = 'Canon_SELPHY_CP1300' # Specify your printer name. If you comment this out, it will print to the first printer it finds. Printer names are printed to std out when you run the photobooth. You can copy one from there if you do not know the name
print_to_pdf = False # Whether to print to a PDF instead of a printer
make_gifs = False   # True to make an animated gif. False to post 4 jpgs into one post.
hi_res_pics = True  # True to save high res pics from camera.
                    # If also uploading, the program will also convert each image to a smaller image before making the gif.
                    # False to first capture low res pics. False is faster.
                    # Careful, each photo costs against your daily Tumblr upload max.
camera_iso = False    # adjust for lighting issues. Normal is 100 or 200. Sort of dark is 400. Dark is 800 max.
                    # available options: 100, 200, 320, 400, 500, 640, 800
black_and_white = False # Set to True to capture in black and white
