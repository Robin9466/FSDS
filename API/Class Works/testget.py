from flask import Flask, request, jsonify
import mysql.connector as conn
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.ERROR)


@app.route("/test")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get('mail_id')
    return "This is my first function for get {} {} {}".format(get_name, mobile_number, mail_id)


@app.route("/fetch_data")
def get_data():
    db = request.args.get('db')
    tn = request.args.get('tn')

    try:
        con = conn.connect(host="localhost", user="root", passwd="*K37759@Others#", database=db)
        cur = con.cursor(dictionary=True)

        query = f'SELECT * FROM {tn}'
        cur.execute(query)

        data = cur.fetchall()

    except Exception as e:
        logging.error(f"Error fetching data: {str(e)}")
        return jsonify({"error": str(e)})
    finally:
        # Close the cursor and connection in a finally block
        if con.is_connected():
            cur.close()
            con.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run()
