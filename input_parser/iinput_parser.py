import abc

class IInputParser(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def get_input_params(self) -> dict:
    pass
