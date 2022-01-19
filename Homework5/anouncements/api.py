from flask import Flask
from flask_restful import (
    reqparse,
    abort,
    Api,
    Resource
)

app = Flask(__name__)
api = Api(app)

ANNOUNCEMENT_STORAGE = {}


def abort_if_doesnt_exist(_id):
    if _id not in ANNOUNCEMENT_STORAGE:
        abort(404, message="Todo {} doesn't exist".format(_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


class Announcement(Resource):
    def get(self, todo_id):
        abort_if_doesnt_exist(todo_id)
        return ANNOUNCEMENT_STORAGE[todo_id]


class AnnouncementList(Resource):
    def get(self):
        return ANNOUNCEMENT_STORAGE

    def post(self):
        args = parser.parse_args()
        announcement_id = int(max(ANNOUNCEMENT_STORAGE.keys()).lstrip('announcement')) + 1
        announcement_id = f'announcement{announcement_id}'
        ANNOUNCEMENT_STORAGE[f'announcement{announcement_id}'] = args['announcement']
        return ANNOUNCEMENT_STORAGE[announcement_id], 201


api.add_resource(AnnouncementList, '/announcements')
api.add_resource(Announcement, '/announcements/<announcement_id>')


if __name__ == '__main__':
    app.run(debug=True)
