ondyq_san = int(input("Ондық санау жүйесіндегі санды енгізіңіз: "))

ekilik_san = ""

while ondyq_san > 0:
    qaldyq = ondyq_san % 2  
    ekilik_san = str(qaldyq) + ekilik_san   
    ondyq_san = ondyq_san // 2  

print("Екілік санау жүйесіндегі сан:", ekilik_san)
