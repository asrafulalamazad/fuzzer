from flask import Flask,jsonify
import base64

app = Flask(__name__)

@app.route("/")
def home():
    return "Is is just a api"

@app.route("/dump/<id>/state")
def state(id):
    s = {
            "id" : id,
            "register":{
                "rax":0x414141414141414141,
                "rip":0x616161616161616161,
                "rbp":0xc0c0c0c0c0c0c0c0c0,
                },
            "disassembly":'''push    rbp
            mov     rbp, rsp
            mov     DWORD PTR [rbp-4], edi
            mov     eax, DWORD PTR [rbp-4]
            imul    eax, DWORD PTR [rbp-4]
            pop     rbp
            ret
            '''
        }
    return jsonify(s)
@app.route("/dump/<id>/memory/<addr>")
def memory(id,addr):
    mem = {
            "id":id,
            "memory":base64.b64encode(bytes("A"*0x1000,"utf-8")).decode("utf-8"),
            "address":addr
            }
    return jsonify(mem)

if __name__ == "__main__":
    app.run(debug=True)
