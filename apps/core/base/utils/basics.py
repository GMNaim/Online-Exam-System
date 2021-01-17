import uuid


def random_hex_code(length: int = 8) -> str:
    """
        To create a new random hex code of dynamic length.

        :parameter
            length (int): set how many character of hex code will generate. Default is 8 character.

        :return
            random hex code with dynamic length.
    """
    return uuid.uuid4().hex[:length]

