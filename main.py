from flask import Flask
from flask_restful import Api, Resource, reqparse
import psycopg2


app = Flask(__name__)
api = Api(app)

# Connect db
conn = psycopg2.connect(dbname="requests",
                       user="me1",
                       password="99@leX216",
                       host="89.223.68.159",
                       port="5432"
)
c = conn.cursor()



class RepairRequests(Resource):


    res = {}
    def get(self):

        c.execute("select * from repair_requests")
        for item in c.fetchall():
            l = len(self.res)
            print(item)

            self.res[l+1]= {"id": item[0],
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
        return self.res

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("ownerName", type=str)
        parser.add_argument("phoneNumber", type=str)
        parser.add_argument("carModel", type=str)
        parser.add_argument("issueDescription", type=str)
        parser.add_argument("date", type=str)
        parser.add_argument("time", type=str)
        parser.add_argument("status", type=str)
        parser.add_argument("completionTime", type=str)
        parser.add_argument("completionDate", type=str)
        bigbob = parser.parse_args()
        print(bigbob)
        return bigbob



api.add_resource(RepairRequests, '/api/repair_requests')
api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
