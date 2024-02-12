import numpy as np
from .utils import Utilities


class RubiesDecoder:

    def __init__(self, encoded_image_path: str) -> None:
        self._encoded_image = Utilities.read_image(encoded_image_path)

        _, _enc_a, _enc_b = Utilities.split_to_lab_components(self._encoded_image)

        _enc_a_mag = Utilities.get_magnitude(_enc_a)
        _enc_b_mag = Utilities.get_magnitude(_enc_b)

        self._diff_a = self._extract_difference(_enc_a_mag)
        self._diff_b = self._extract_difference(_enc_b_mag)

        self._decoded_a: np.ndarray = None
        self._decoded_b: np.ndarray = None
    
    def decode(self, **kwargs) -> tuple[np.ndarray]:
        secret_image_a = self._deinsert(self._diff_a, **kwargs)
        secret_image_b = self._deinsert(self._diff_b, **kwargs)

        self._decoded_a = Utilities.scale_back_from_float64_to_uint8(secret_image_a)
        self._decoded_b = Utilities.scale_back_from_float64_to_uint8(secret_image_b)

        return (self._decoded_a, self._decoded_b)
    
    def save(self, path_a: str, path_b: str) -> None:
        if self._decoded_a is None or self._decoded_b is None:
            raise ValueError("You should decode the images first.")
        Utilities.save_image(self._decoded_a, path_a)
        Utilities.save_image(self._decoded_b, path_b)

    @staticmethod
    def _extract_difference(modified_mag) -> np.ndarray:
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
        raise NotImplementedError("This method should be implemented in the child class.")