from mycroft import MycroftSkill, intent_file_handler


class EmergencyCall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('call.emergency.intent')
    def handle_call_emergency(self, message):
        self.speak_dialog('call.emergency')


def create_skill():
    return EmergencyCall()

