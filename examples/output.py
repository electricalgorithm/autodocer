Here is the documentation for the provided code:
```markdown
# RubiesDecoder

class RubiesDecoder:
    """
    Decodes a pair of modified images and saves them as two separate images.
    """

    def __init__(self, encoded_image_path: str) -> None:
        """
        Initializes the decoder with an encoded image path.
        :param encoded_image_path: The path to the encoded image.
        """
        self._encoded_image = Utilities.read_image(encoded_image_path)

    def decode(self, **kwargs) -> tuple[np.ndarray]:
        """
        Decodes the images and returns them as a tuple of two numpy arrays.
        :param kwargs: Keyword arguments for customizing the decoding process.
        :return: A tuple of two numpy arrays containing the decoded images.
        """
        secret_image_a = self._deinsert(self._diff_a, **kwargs)
        secret_image_b = self._deinsert(self._diff_b, **kwargs)

        self._decoded_a = Utilities.scale_back_from_float64_to_uint8(secret_image_a)
        self._decoded_b = Utilities.scale_back_from_float64_to_uint8(secret_image_b)

        return (self._decoded_a, self._decoded_b)

    def save(self, path_a: str, path_b: str) -> None:
        """
        Saves the decoded images to two separate files.
        :param path_a: The path to the first decoded image.
        :param path_b: The path to the second decoded image.
        """
        if self._decoded_a is None or self._decoded_b is None:
            raise ValueError("You should decode the images first.")
        Utilities.save_image(self._decoded_a, path_a)
        Utilities.save_image(self._decoded_b, path_b)

    @staticmethod
    def _extract_difference(modified_mag) -> np.ndarray:
        """
        Extracts the difference between two modified images and returns it as a numpy array.
        :param modified_mag: The modified magnitude of the images.
        :return: The difference between the two modified images.
        """
        average = np.mean(modified_mag)
        to_delete = 300
        modified_mag[0:to_delete, 0:to_delete] = average
        modified_mag[-to_delete:, -to_delete:] = average
        modified_mag[0:to_delete, -to_delete:] = average
        modified_mag[-to_delete:, 0:to_delete] = average
        modified_mag[modified_mag < average] = average
        return modified_mag - np.mean(modified_mag)

    @staticmethod
    def _deinsert() -> np.ndarray:
        """
        Implements the custom decoding logic for the RubiesDecoder class.
        This method should be implemented in the child class.
        :return: The decoded image.
        """
        raise NotImplementedError("This method should be implemented in the child class.")