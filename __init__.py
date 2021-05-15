from mycroft import MycroftSkill, intent_handler


class NextcloudCalendar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('calendar.nextcloud.intent')
    def handle_calendar_nextcloud(self, message):
        self.speak_dialog('calendar.nextcloud')
        
        self.log.info("I am a DEBUG INformation")


def create_skill():
    return NextcloudCalendar()

