from PIL import Image, ImageChops


def assert_image_almost_equal(img_left: str, img_right: str):
    image1 = Image.open(img_left)
    image2 = Image.open(img_right)
    diff = ImageChops.difference(image1, image2)
    if diff.getbbox() is not None:
        raise AssertionError('two image are not almost equal!')


if __name__ == '__main__':
    import click

    @click.command()
    @click.argument('image_left', type=click.Path(exists=True))
    @click.argument('image_right', type=click.Path(exists=True))
    def test_two_image_almost_equal(image_left, image_right):
        try:
            assert_image_almost_equal(image_left, image_right)
        except AssertionError:
            raise
        else:
            print('tow image are almost equal.')

    test_two_image_almost_equal()
