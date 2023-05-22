from flask import Flask, jsonify, request, make_response # Importa a biblioteca
import pymysql.cursors

app = Flask(__name__) # Inicializa a aplicação

@app.route('/', methods=["GET", "OPTIONS"]) # Cria uma rota
def main():
  if request.method == "OPTIONS":
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response
  res = jsonify({"message": "Hello Server"})
  res.headers.add("Access-Control-Allow-Origin", "*")
  return res

@app.route('/usuarios', methods=["POST", "GET"])
def pedidos():
    connection = pymysql.connect(
       host="localhost",
       port=3306,
       user="root",
       password="",
       database="usuarios",
       cursorclass=pymysql.cursors.DictCursor
    )

    with connection:
      if request.method == "POST":
        body = request.json
        with connection.cursor() as cursor:
          sql = "INSERT INTO `usuario` (`nome`) VALUES (%s)" 

          cursor.execute(sql, (body["nome"]))
        connection.commit()
        return "Entrada Adicionada"

      if request.method == "GET":
        with connection.cursor() as cursor:
          sql = "SELECT * FROM `usuario`"
          cursor.execute(sql)
          result = cursor.fetchall()
          return result

if __name__ == '__main__':
  app.run() # Executa a aplicação