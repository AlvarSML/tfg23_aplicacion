import torchvision.transforms as transforms

def get_padding(image):
    """ Crea la transformacion para añador bordes a "0"
    """
    max_w = 1500
    max_h = 1500
    
    height, width = image.size
    h_padding = (max_w - height) / 2
    v_padding = (max_h - width) / 2
    l_pad = h_padding if h_padding % 1 == 0 else h_padding+0.5
    t_pad = v_padding if v_padding % 1 == 0 else v_padding+0.5
    r_pad = h_padding if h_padding % 1 == 0 else h_padding-0.5
    b_pad = v_padding if v_padding % 1 == 0 else v_padding-0.5
    
    padding = (int(l_pad), int(t_pad), int(r_pad), int(b_pad))
    
    return padding

def pad_image(self, image):
        padded_im = pad(image, get_padding(image)) # torchvision.transforms.functional.pad
        return padded_im
    
class Padding(object):
    """ Clase para poder añadir la transformacion Padding al pipeline
    """
    def __init__(self, fill=0, padding_mode='constant'):
        self.fill = fill
        self.padding_mode = padding_mode
    
    def __call__(self, img):
        """
        Args:
            img (PIL Image): Image to be padded.

        Returns:
            PIL Image: Padded image.
        """
        return transforms.functional.pad(img, get_padding(img), self.fill, self.padding_mode)
    
    def __repr__(self):
        return self.__class__.__name__ + '(padding={0}, fill={1}, padding_mode={2})'.\
            format(self.fill, self.padding_mode)