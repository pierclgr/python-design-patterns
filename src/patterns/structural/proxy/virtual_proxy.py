# Virtual Proxy: a proxy that appears to be the underlying-initialized object that it masks, but in reality it is an
# object that masquerades the underlying functionality of the true object; it can also offer additional functionalities

class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")

def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")

# this code works, but if we don't call the image.draw(), the constructor of image will still load the image, which is
# expensive

# in this scenario, we can add a proxy that adds this functionality of "smart" loading, without modifying the Bitmap
# class such that we can use the proxy as a drop-in replacement for the Bitmap class; the proxy will lazily load the
# image

class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self.__bitmap = None

    def draw(self):
        if not self.__bitmap:
            self.__bitmap = Bitmap(self.filename)
        self.__bitmap.draw()


if __name__ == "__main__":
    bmp = Bitmap("hello.jpg")
    draw_image(bmp)

    # the loading now happens within draw_image
    bmp = LazyBitmap("hello_2.jpg")

    # the loading specifically happens in the first call of draw_image (this one)
    draw_image(bmp)
    draw_image(bmp)

# this looks similar to a decorator, however:
# - proxy provides IDENTICAL interface, decorator provides ENHANCED interface
# - proxy might not even be working with materialized objects and/or have references to them
# - decorator is specifically designed to add functionality