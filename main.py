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
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        
        c.execute("select * from repair_requests")
        for item in c.fetchall():
            l = len(res)

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

    def post(self):
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("ownerName", type=str)
        parser.add_argument("phoneNumber", type=str)
        parser.add_argument("carModel", type=str)
        parser.add_argument("issueDescription", type=str, required=False)
        parser.add_argument("date", type=str)
        parser.add_argument("time", type=str)
        args = parser.parse_args()
        if args["issueDescription"]:
            if args["issueDescription"] == "":
                    args["issueDescription"] = "Не указана"
            if args["issueDescription"] is None:
                    args["issueDescription"] = "Не указана"
            if args["issueDescription"] == " ":
                    args["issueDescription"] = "Не указана"
        else:
            args["issueDescription"]="Не указана"

        c.execute(
            """INSERT INTO public.repair_requests("ownerName", "phoneNumber", "carModel", "issueDescription","date", "time") VALUES(%s,%s,%s,%s,%s,%s)""",
            (args["ownerName"],
             args["phoneNumber"],
             args["carModel"],
             args["issueDescription"],
             args["date"],
             args["time"]
             )
        )
        conn.commit()
        c.close()

class DeleteRepairRequests(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        args = parser.parse_args()
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        c.execute(f"""DELETE FROM public.repair_requests WHERE id = {args["id"]}""")
        conn.commit()
        c.close()

    def get(self):
        return {"result":"deleted"}

class DoneRepairRequests(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "id", type=int
        )
        args = parser.parse_args()
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        c.execute(f"""
                    UPDATE public.repair_requests 
                    SET status = 'выполнено'
                    WHERE id = {args["id"]}
        """)
        conn.commit()
        c.close()

class EditRepairRequests(Resource):
    def post(self):
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("ownerName", type=str)
        parser.add_argument("phoneNumber", type=str)
        parser.add_argument("carModel", type=str)
        parser.add_argument("issueDescription", type=str, required=False)
        parser.add_argument("date", type=str)
        parser.add_argument("time", type=str)
        parser.add_argument("id",type=int)
        args = parser.parse_args()

        c.execute(
            """UPDATE public.repair_requests
            SET ownerName = %s, 
            SET phoneNumber = %s,
            SET carModel = %s,
            SET issueDescription = %s,
            SET date = %s,
            SET time = %s
            WHERE id = %s""",
            (args["ownerName"],
             args["phoneNumber"],
             args["carModel"],
             args["issueDescription"],
             args["date"],
             args["time"],
             args["id"]
             )
        )
        conn.commit()
        c.close()


class PaintingRequests(Resource):

    def get(self, status=0):
        res = {}
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        
        c.execute("select * from painting_requests")
        
        for item in c.fetchall():
            l = len(res)


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

    def post(self):
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        parser = reqparse.RequestParser()
        parser.add_argument("ownerName", type=str)
        parser.add_argument("phoneNumber", type=str)
        parser.add_argument("carModel", type=str)
        parser.add_argument("color", type=str, required=False)
        parser.add_argument("date", type=str)
        args = parser.parse_args()
        c.execute("""
            INSERT INTO public.painting_requests("ownerName", "phoneNumber", "carModel", "color", "date") VALUES(%s,%s,%s,%s,%s)
        """,(
            args["ownerName"],
            args["phoneNumber"],
            args["carModel"],
            args["color"],
            args["date"]
        ))
        conn.commit()
        c.close()

class DeletePaintingRequests(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", type=int)
        args = parser.parse_args()
        conn = psycopg.connect(dbname="requests",
                               user="sanekakf",
                               password="99mir216",
                               host="95.31.5.158",
                               port="5432")
        c = conn.cursor()
        c.execute(f"""DELETE FROM public.painting_requests WHERE id = {args["id"]}""")
        conn.commit()
        c.close()

class DonePaintingRequests(Resource):
    def get(self):
        pass

class EditPaintingRequests(Resource):
    def post(self):
        pass

api.add_resource(RepairRequests, '/api/repair_requests')
api.add_resource(DeleteRepairRequests, '/api/repair_requests/delete')
api.add_resource(DoneRepairRequests, '/api/repair_requests/done')
api.add_resource(EditRepairRequests, '/api/repair_requests/edit')
api.add_resource(PaintingRequests, '/api/painting_requests')
api.init_app(app)


@app.route("/")
def hello():
    return "Салтыков + Аферов = 😎"


if __name__ == '__main__':
    port = 8080
    app.run(debug=True, host='0.0.0.0', port=port)
