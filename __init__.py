from mycroft import MycroftSkill, intent_file_handler


class NextcloudCalendar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calendar.nextcloud.intent')
    def handle_calendar_nextcloud(self, message):
        self.speak_dialog('calendar.nextcloud')


def create_skill():
    return NextcloudCalendar()

