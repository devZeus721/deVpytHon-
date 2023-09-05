import qrcode

def generate_qr_code(data, filename):
    """Generates a QR code from the given data and saves it as an image file.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str): The name of the file to save the QR code image.

    Returns:
        None
    """
    try:
        # Create qr code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Add data
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        # Save it
        img.save(filename)
    except Exception as e:
        print(f"Error generating QR code: {e}")