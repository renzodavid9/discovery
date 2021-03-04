from script_manager.default_script_manager import DefaultScriptManager

class ScriptManagerFactory():
  @staticmethod
  def get_script_manager(config, message_sender):
    return DefaultScriptManager(config, message_sender)