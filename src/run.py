import sys
from app import create_app


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'reset':
        app = create_app(reset=True)
    else: 
        app = create_app()
    # run the app    
    app.run(debug=True)