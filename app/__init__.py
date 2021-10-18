from flask import Flask
"""""
When a MVC desing pattern is implemented some changes must be undertaken, in order to avoid circular imports, 
in this paricular case the importing of views was written at the bottom of this file, if this was done the 
other way around Errors will pop out, making paths unavailable.
"""""
app = Flask(__name__)

from app import views