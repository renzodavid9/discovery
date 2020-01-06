import abc

class IInputParser(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def get_input_params(self) -> dict:
    """Returns the list of arguments used to run the script."""
    pass
