from . import internet

class PhishTank:

    def __init__(self):
        self.db_update_url = r"http://data.phishtank.com/data/online-valid.json"
        self.internet = internet.AsyncInternet()

    def update_db(self):
        response = self.internet.get(self.db_update_url)
        return response
        # todo: write this to a db
        # sqlite?

