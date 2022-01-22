
class Announcement:
    '''violates Single resposibility'''
    def __init__(self, announcement: dict):
        self.announcement = announcement

    def get_announcement_info(self):
        return self.announcement['info']

    def save(self):
      pass


class AnnouncementCheck:
    ''' proper Single resposibility '''

    def __init__(self, announcement: dict):
        self.announcement = announcement

    def get_announcement_info(self):
        return self.announcement['info']


class AnnouncementDB:
    ''' proper of Single resposibility '''

    def __init__(self, announcement: dict):
        self.announcement = announcement

    def save(self):
        pass
