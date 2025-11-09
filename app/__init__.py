from flask import Flask, render_template
import config

def create_app():
    app = Flask(__name__)

    @app.before_request
    def check_for_maintenance():
        if config.MAINTENANCE_MODE:
            return render_template("maintenance.html"), 503
        

    from .basic.routes import basic_bp
    app.register_blueprint(basic_bp)

    from .allPdf.routes import allPdf_bp
    app.register_blueprint(allPdf_bp)

    return app