from flask import Flask
from flask_restful import Api, Resource, reqparse
import psycopg

app = Flask(__name__)
api = Api(app)


# Connect db


class RepairRequests(Resource):

    def get(self):
        res = {}
        conn = psycopg.connect(dbname="requests",
                               user="me1",
                               password="99@leX216",
                               host="89.223.68.159",
                               port="5432"
                               )
        c = conn.cursor()
        c.execute("select * from repair_requests")
        for item in c.fetchall():
            l = len(res)
            print(item)

            res[l + 1] = {"id": item[0],
                          "ownerName": item[1],
                          "phoneNumber": item[2],
                          "carModel": item[3],
                          "issueDescription": item[4],
                          "date": item[5].strftime("%Y-%m-%d"),
                          "time": item[6],
                          "status": item[7],
                          "completionTime": item[8],
                          "completionDate": item[9]
                          }
        conn.close()
        return res

class PaintingRequests(Resource):

    def get(self):
        res = {}
        conn = psycopg.connect(dbname="requests",
                               user="me1",
                               password="99@leX216",
                               host="89.223.68.159",
                               port="5432"
                               )
        c = conn.cursor()
        c.execute("select * from painting_requests")
        for item in c.fetchall():
            l = len(res)
            print(item)

            res[l + 1] = {"id": item[0],
                          "ownerName": item[1],
                          "phoneNumber": item[2],
                          "carModel": item[3],
                          "color": item[4],
                          "date": item[5].strftime("%Y-%m-%d"),
                          "status": item[6],
                          }
        conn.close()
        return res


api.add_resource(RepairRequests, '/api/repair_requests')
api.add_resource(PaintingRequests, '/api/painting_requests')
api.init_app(app)


@app.route("/")
def hello():
    return "Timeweb Cloud + Flask = ❤️"


if __name__ == '__main__':
    port = 8080
    app.run(debug=True, host='0.0.0.0', port=port)
