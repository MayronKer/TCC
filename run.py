# conectando MVC
import views
from views import app


import controllers


# definindo o que fazer ao inicial o software
if __name__ == "__main__":
    app.debug = True
    app.run()
