# services/errors.py

class UserRegistrationEmailAlreadyBeingUsedError(Exception):
    """Exception raised when attempting to register with an existing email."""
    pass

class UserRegistrationUsernameAlreadyBeingUsedError(Exception):
    """Exception raised when attempting to register with an existing username."""
    pass

class UserLoginWrongPasswordError(Exception):
    """Exception raised when the password is incorrect during login."""
    pass

class UserLoginEmailDoesNotExistError(Exception):
    """Exception raised when the email does not exist during login."""
    pass