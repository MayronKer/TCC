# conectando MVC
from models import app

# definindo o que fazer ao inicial o software
if __name__ == "__main__":
    app.debug = True
    app.run()
